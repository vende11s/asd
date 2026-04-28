def partition(A, start, end):
    pivot = A[end]

    i = start-1
    for j in range(start, end):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[end], A[i+1] = A[i+1], A[end]
    return i+1

def _quickselect(A, start, end, k):
    pivot_idx = partition(A, start, end)

    if pivot_idx == k:
        return A[k]
    
    if pivot_idx > k:
        return _quickselect(A, start, pivot_idx - 1, k)
    else:
        return _quickselect(A, pivot_idx + 1, end, k)
    

def quickselect(A, k):
    return _quickselect(A, 0, len(A)-1, k)

T = [2,1,6,3,7]

print(quickselect(T, 0))