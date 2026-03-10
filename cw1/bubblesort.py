### buble sort

def bubble(T)->list:
    for i in range(0, len(T)):
        for j in range(0, len(T)-i-1):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
        
T = [2,1,3,7,6,9,6,7]
bubble(T)
print(T)