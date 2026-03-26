'''
quick sort bez rekurencji
'''

def _quicksort(A, start, end):
    if not start < end:
        return None
    
    middle = _partition(A, start, end)
    _quicksort(A, start, middle-1)
    _quicksort(A, middle+1, end)

def nonrek_quicksort(A):
    stack = []

    stack.append(_partition(A,0,len(A)-1))
    while stack:
        last_pivot = stack.pop()
        if



    

