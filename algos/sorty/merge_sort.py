def _merge(A, B, start, mid, end):
    midCopy = mid
    startCopy = start

    b_ind = start
    while start < midCopy and mid <= end:
        if A[start] <= A[mid]:
            B[b_ind] = A[start]
            start+=1
        else:
            B[b_ind] = A[mid]
            mid+=1
        
        b_ind+=1
    
    while start < midCopy:
        B[b_ind] = A[start]

        start+=1
        b_ind+=1

    while mid <= end:
        B[b_ind] = A[mid]

        mid+=1
        b_ind+=1

    for i in range(startCopy, end+1):
        A[i] = B[i]


# recursion logic
def _mergesort(A, B, start, end):
    if start>=end:
        return

    mid = (start+end)//2
    _mergesort(A, B, start, mid)
    _mergesort(A, B, mid+1, end)

    _merge(A,B, start, mid+1, end)

# wrapper around logic
def mergesort(T):
    n = len(T)

    # list for caching temporary data
    cache = [0 for _ in range(n)]
    _mergesort(T, cache, 0, n-1)


T = [2,1,3,7,4,2,0]
mergesort(T)
print(T)

