# podejscie proste, da sie tym sortowac tylko liczby (calych obiektow sie nie da)
# niestabilne - nie mozna uzyc do Radix Sorta
def simple_counting_sort(A, m):
    counter = [0] * m
    for x in A:
        counter[x]+=1
    
    ind = 0
    for i in range(m):
        while counter[i] > 0:
            A[ind] = i
            ind += 1
            counter[i]-=1

    return A

def counting_sort(A):
    max_val = max(A)
    counter = [0] * (max_val + 1)
    result = [0] * len(A)
    
    # zliczanie
    for x in A:
        counter[x] += 1
        
    # Sumy prefiksowe
    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]
    # Od tego momentu w C[x] jest liczba elementow mniejsza lub rowna x
        
    # ukladanie zliczonyych elementow - trzeba isc od tylu zeby byla stabilnosc
    for i in range(len(A) - 1, -1, -1):
        x = A[i]
        
        counter[x] -= 1
        # 1. zmniejszamy miejsce bo indeksujemy od 0 
        # (jak mamy jedną jedynke i jest to najmniejsza liczba to C[1] = 1, trzeba odjac zeby bylo 0)
        # 2. jak mamy np. cztery zera to zmniejszamy indeks dla kolejnego zera

        target_ind = counter[x]
        # wstawiamy oryginalny element na jego nowe miejsce w B
        result[target_ind] = x
        
    return result


