# radix sort dla liczb
# najpierw se ogarnij wersje dla stringow, tam jest lepiej powytlumaczane wszystko
def counting_sort(A, result, exp):
    counter = [0] * 10  # 10 cyfr nie musimy trzymac miejsca dla braku cyfry
                        # bo 5 to to samo co 00005, wiec brak cyfry = 0

    for x in A:
        digit = (x // exp) % 10
        counter[digit] += 1
    
    for j in range(1, 10):
        counter[j] += counter[j - 1]

    for j in range(len(A)-1, -1, -1):
        digit = (A[j] // exp) % 10
        counter[digit] -= 1
        ind = counter[digit]

        result[ind] = A[j]

def radix_sort(A):
    max_num = max(A)
    B = [0] * len(A)
    
    exp = 1
    while max_num // exp > 0:
        counting_sort(A, B, exp)
        exp *= 10
        A, B = B, A 

    return A