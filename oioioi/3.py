#### vibe code 1st try B)))
import sys
from array import array
from itertools import accumulate

def main():
    def get_input():
        for line in sys.stdin.buffer:
            for word in line.split():
                yield int(word)

    tokens = get_input()
    
    try:
        n = next(tokens)
    except StopIteration:
        return

    T = array('i', [0]) * n
    for i in range(n):
        T[i] = next(tokens)

    buf = array('i', [0]) * n
    
    for shift in (0, 16):
        count = [0] * 65536
        
        for x in T:
            count[(x >> shift) & 0xFFFF] += 1
        
        count = [0] + list(accumulate(count[:-1]))
        
        for x in T:
            idx = (x >> shift) & 0xFFFF
            buf[count[idx]] = x
            count[idx] += 1
            
        T, buf = buf, T

    del buf
    
    try:
        q = next(tokens)
    except StopIteration:
        return

    out_buffer = []
    for _ in range(q):
        try:
            qi = next(tokens)
            out_buffer.append(str(T[n - qi]))
            
            if len(out_buffer) >= 5000:
                sys.stdout.write('\n'.join(out_buffer) + '\n')
                out_buffer = []
        except StopIteration:
            break
            
    if out_buffer:
        sys.stdout.write('\n'.join(out_buffer) + '\n')

if __name__ == "__main__":
    main()