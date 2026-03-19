"""
Drzewo do liczenia sum prefixowych ale z szybkimi updeatami

Inna nazwa: binary indexed tree

Złożoność pamięciowa: O(n)
Złożoność obliczeniowa:
    update: O(log n)
    query: O(log n)

Takie drzewo punkt-przedział, ale:
    lepsza złożoność pamięciowa
    mniejsza stała w złożoności
    służy tylko do liczenia sum prefiksowych

indexowane od 1
"""

# least significant bit
def LSB(i):
    return i & -i

def update(FenT, i, to_add):
    while i < len(FenT):
        FenT[i] += to_add
        i += LSB(i)

# sum arr from [1 to i]
def query(FenT, i):
    result = 0
    while i != 0:
        result += FenT[i]
        i -= LSB(i)
    return result

########## USE CASE ##########
T = [5,3,2,6,1,3,1,1,1,1,2]

FenT = [0] * (len(T)+1)

max_found = 0
for x in T:
    max_found = max(max_found, query(FenT, x))
    update(FenT, x+1, 1)

print(max_found)
