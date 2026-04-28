# Radix Sort do sortowania stringow

def charInd(x):
    return ord(x) - ord('a')

# sortowananie tablicy stringow po znaku na pozycji 'i'
def counting_sort(A, result, i):
    counter = [0] * 27

    '''
        26 znakow w alfabecie + 1 dla przypadku gdy na pozycji 'i' w jakims stringu
        nie ma znaku (jest krotszy)

        w sortowaniu leksykograficznym gdy na pozycji 'i' nie ma zadnego znaku
        to jest to element 'mniejszy' od elementu ktory ma tam jakis znak:

        aaa < aaaa

        dlatego counter[0] to bedzie miejsce w ktorym bedziemy trzymac brak znaku.
        counter[1] to jest 'a', a counter[26] to jest 'z'
    '''

    # zliczanie
    for s in A:
        if len(s) <= i:
            counter[0] += 1
            continue

        ind = charInd(s[i]) + 1 # +1 bo znaki są przesuniete o 1 w prawo
                                # aby bylo miejsce dla braku znaku
        counter[ind] += 1
    
    # liczenie sum prefiksowych
    for j in range(1, len(counter)):
        counter[j] += counter[j - 1]

    for j in range(len(A)-1, -1, -1): # idziemy od konca zeby zachowac stabilnosc
        if len(A[j]) <= i:
            counter[0] -= 1
            ind = counter[0]

            result[ind] = A[j]
            continue

        char_idx = charInd(A[j][i]) + 1
        counter[char_idx] -= 1
        ind = counter[char_idx]

        result[ind] = A[j]
    
    return result

def radix_sort(A):
    max_len = 0
    for s in A:
        max_len = max(max_len, len(s))
    
    B = [""] * len(A) # bufor zeby za kazdym razem nie tworzyc nowej listy
    # zamysl jak w merge sort z wykladu
    for i in range(max_len - 1, -1, -1):
        counting_sort(A, B, i)

        A,B = B,A # ping pong

    return A