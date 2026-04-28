def _partition(A, start, end):
    pivot = A[end] # taking last element as pivot
    swap_index = start-1

    for i in range(start, end+1): # end+1 cuz end is inclusive
        if A[i] <= pivot:
            swap_index += 1
            A[i], A[swap_index] =  A[swap_index], A[i]

    return swap_index # current pos of pivot

def _quicksort(A, start, end):
    if not start < end:
        return None
    
    middle = _partition(A, start, end)
    _quicksort(A, start, middle-1)
    _quicksort(A, middle+1, end)

# wrapper around logic
def quicksort(A):
    _quicksort(A, 0, len(A)-1) 

def ogrodzenie(M,D,T):
    quicksort(T)

    result = 0
    for i in range(1, len(T)):
        if T[i] - T[i-1] >= D:
            result += 1
    
    return result