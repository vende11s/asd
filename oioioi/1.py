import sys
from random import randint, seed
import bisect

OIOIOI = True

def solution(T):
    # least significant bit
    def LSB(i):
        return i & -i

    def update(FenT, i, to_add):
        while i < len(FenT):
            FenT[i] += to_add
            i += LSB(i)

    # sum arr from [1 to i]
    def query(FenT, i):
        result = 0
        while i != 0:
            result += FenT[i]
            i -= LSB(i)
        return result
    
    unique_T = sorted(list(set(T)))
    ranks = {s: i+1 for i, s in enumerate(unique_T)}
    
    FenT = [0] * (len(unique_T) + 2)
    max_found = 0
    for s in T:
        x = ranks[s]
        max_found = max(max_found, query(FenT, x-1))
        update(FenT, x, 1)
    
    return max_found
        

if __name__ == "__main__":
    def generate_random_string(length):
        return ''.join(chr(randint(97, 122)) for _ in range(length))
    
    if OIOIOI:
        n = int(sys.stdin.readline().strip())
        words = [sys.stdin.readline().strip() for _ in range(n)]
        print(solution(words))
    else:
        seed(1)
        test_def = [
            (10, 5, 10, 6),
            (100, 5, 10, 88),
            (100, 20, 100, 91),
            (10000, 10, 30, 9901)
        ]
        ok = 0
        for idx, (n, m_low, m_high, ans) in enumerate(test_def):
            print("Test", idx + 1)
            words = [generate_random_string(randint(m_low, m_high)) for _ in range(n)]
            result = solution(words)
            if result == ans:
                print("OK")
                ok += 1
            else:
                print("Błąd!")
        print("Wynik:", ok, "/", len(test_def))