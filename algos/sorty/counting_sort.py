# podejscie proste, da sie tym sortowac tylko liczby (calych obiektow sie nie da)
# niestabilne 
def simple_counting_sort(A, m):
    B = [0] * m
    for x in A:
        B[x]+=1
    
    ind = 0
    for i in range(m):
        while B[i] > 0:
            A[ind] = i
            ind += 1
            B[i]-=1

    return A


