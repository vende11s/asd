# traversing the heap
def parent(i): return (i-1)//2
def left(i): return (i*2)+1
def right(i): return (i*2)+2

def _heapify(A, i, end = -1):
    if end == -1:
        end = len(A)
    max_ind = i

    if left(i) < end and A[left(i)] > A[i]:
        max_ind = left(i)
    
    if right(i) < end and A[right(i)] > A[max_ind]:
        max_ind = right(i)
    
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        _heapify(A, max_ind, end)

def _build_heap(A):
    for i in range(parent(len(A)-1), -1, -1):
        _heapify(A,i)

def heapsort(A):
    _build_heap(A)
    n = len(A)-1

    for i in range(n):
        A[0], A[n-i] = A[n-i], A[0]
        _heapify(A, 0, n-i)

T = [2,1,3,7,4,2,0]
heapsort(T)
print(T)
