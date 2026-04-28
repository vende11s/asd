def insertion_sort(A):
    for i in range(1, len(A)):
        if A[i] > A[i-1]:  # jak aktualny element jest wiekszy od poprzedniego
            continue       # to wszystko jest git idziemy dalej

        for j in range(i, 0, -1):
            if A[j] > A[j - 1]:
                break
            A[j], A[j - 1] = A[j - 1], A[j]
    
    return A

# m to liczba kubelkow, zazwyczaj powinno to byc len(A)
def bucket_sort(A, m):
    max_val = max(A)
    min_val = min(A)

    buckets = [[] for _ in range(m)]
    
    # wrzucamy elementy do kubelkow
    for x in A:
        scale = (x - min_val) / (max_val - min_val) # od 0.0 do 1.0, mowi nam w ktorym miejscu listy jestesmy
        bucket_idx = int(scale * (m - 1)) # jestesmy np. w 0.7 naszego zakresu, mamy 11 kubelkow
                                          # wiec x trafia do 8 kubelka (m-1 bo indexujemy od 0)
        buckets[bucket_idx].append(x)
    
    # sortujemy elementy wewnatrz kubelkow
    # uzywamy insertion sorta bo w kubelkach jest malo elementow
    # w praktyce jak jest faktycznie rozklad jednostajny to bedzie najszybszy
    for bucket in buckets:
        bucket = insertion_sort(bucket)
    
    # nadpisujemy elementy z kubelkow sportoem do A
    A_idx = 0
    for bucket in buckets:
        for x in bucket:
            A[A_idx] = x
            A_idx += 1
    return A

T = [2,1,3,7,4,2,0,6,7]
print(bucket_sort(T, len(T)))

