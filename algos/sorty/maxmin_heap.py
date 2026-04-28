# traversing the heap
def parent(i): return (i-1)//2
def left(i): return (i*2)+1
def right(i): return (i*2)+2

def heapify_max(A, i, end = -1):
    if end == -1:
        end = len(A)
    max_ind = i

    if left(i) < end and A[left(i)] > A[i]: # change > to < for min heap
        max_ind = left(i)
    
    if right(i) < end and A[right(i)] > A[max_ind]: # change > to < for min heap
        max_ind = right(i)
    
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify_max(A, max_ind, end)

def build_heap_max(A):
    for i in range(parent(len(A)-1), -1, -1):
        heapify_max(A,i)


