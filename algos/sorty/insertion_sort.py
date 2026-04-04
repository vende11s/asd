def insertion_sort(A):
    for i in range(1, len(A)):
        if A[i] > A[i-1]:  # jak aktualny element jest wiekszy od poprzedniego
            continue       # to wszystko jest git idziemy dalej

        for j in range(i, 0, -1):
            if A[j] > A[j - 1]:
                break
            A[j], A[j - 1] = A[j - 1], A[j]
    
    return A


T = [2, 1, 3, 7, 4, 2, 0]
print(insertion_sort(T))