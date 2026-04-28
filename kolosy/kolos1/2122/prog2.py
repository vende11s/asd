def charIdx(c):
    return ord(c) - ord('a')

# i to pozycja po ktorej sortujemy
def counting_sort(T, i):
    counter = [0] * 27 # 26 znakow i index 0 dla przypadku bez znaku
    result = [""] * len(T)
    # zliczanie
    for s in T:
        if len(s) <= i:
            counter[0]+=1
            continue
        counter[charIdx(s[i]) + 1] +=1

    # sumy prefiksowe
    for j in range(1, len(counter)):
        counter[j] += counter[j - 1]

    for j in range(len(T)-1, -1, -1):
        if len(T[j]) <= i:
            counter[0] -= 1
            result[counter[0]] = T[j]
            continue
        
        counter[charIdx(T[j][i]) + 1] -= 1
        idx = counter[charIdx(T[j][i]) + 1]
        result[idx] = T[j]

    return result

def radix_sort(T):
    max_len = 0
    for s in T:
        max_len = max(max_len, len(s))

    for i in range(max_len-1, -1,-1):
        T = counting_sort(T,i)

    return T

def g(T):
    # normalizacja stringow
    for i in range(T):
        T[i] = min(T[i], T[i][::-1])

    T = radix_sort(T)

    result = 1
    current = 1
    
    for i in range(1, len(T)):
        if T[i] != T[i - 1]:
            current = 1
            continue

        current+=1
        result = max(result, current)

    return result


    