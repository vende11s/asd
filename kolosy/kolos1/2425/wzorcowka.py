def insertion_sort(T):
    for i in range(1,len(T)):
        if T[i] > T[i - 1]:
            continue

        for j in range(i, 0, -1):
            if T[j] < T[j-1]:
                T[j], T[j - 1] = T[j - 1], T[j]
            else: break
    return T

def bucket_sort(T):
    min_val = min(T)
    max_val = max(T)

    bucket_amount = len(T)
    buckets = [[] for _ in range(bucket_amount)]
    bucket_size = (max_val - min_val) // bucket_amount
    for i in range(len(T)):
        bucket_idx = int((T[i] - min_val) / bucket_size)
        if bucket_idx == bucket_amount:
            bucket_idx -= 1
        
        buckets[bucket_idx].append(T[i])
    
    for bucket in buckets:
        insertion_sort(bucket)
    
    T_i = 0
    for bucket in buckets:
        for x in bucket:
            T[T_i] = x
            T_i += 1
        
def ogrodzenie(M,D,T):
    bucket_sort(T)
    
    result = 0
    for i in range(1, len(T)):
        if T[i] - T[i-1] >= D:
            result += 1

    return result