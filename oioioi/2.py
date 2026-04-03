import sys

def solve():
    # 1. Zamiast mapować w pętli, rzucamy 'map' na całość od razu - działa w prędkości C
    data = list(map(int, sys.stdin.read().split()))
    
    if not data:
        return

    # 2. Totalny gamechanger: List slicing.
    # Zamiast bawić się w pętle po range(), wycinamy co drugi element.
    # data[2::2] weźmie a_i, data[3::2] weźmie b_i
    starts = [(x, 0) for x in data[2::2]]
    ends = [(x, 1) for x in data[3::2]]
    
    # 3. Łączenie list plusem jest w Pytonie zoptymalizowane pod maską
    events = starts + ends
    
    # Sortowanie (wbudowane Timsort z Pythona jest mega szybkie)
    events.sort()

    if not events:
        return

    best_ind = events[0][0]
    best = 1
    curr = 0

    for pos, typ in events:
        if typ == 0:
            curr += 1
           
            if curr >= best:
                best = curr
                best_ind = pos
        else:
            curr -= 1
            
    print(best, best_ind)

if __name__ == "__main__":
    solve()