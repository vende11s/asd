'''
s...
c...
..ce

mamy takiego grida n x m
zaczynamy w s, szukamy najkrotszej drogi do e
nie możemy wejść do c

dla ulatwienia i mniej ifow nie chodzimy po skosie,
tylko gora dol prawo lewo
'''

from collections import deque

def bfs_grid(G, s):
    rows = len(G)
    cols = len(G[0])
    
    # kolejka przechowuje: (wiersz, kolumna, dystans)
    q = deque()
    q.append((s[0], s[1], 0))
    
    # set trzyma odwiedzone pola, zeby nie chodzic w kolko
    visited = set()
    visited.add(s)
    
    # mozliwe ruchy: gora, dol, lewo, prawo
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    while q:
        r, c, dist = q.popleft()
        
        # jak trafilismy na koniec, to od razu zwracamy liczbe krokow
        if G[r][c] == 'e':
            return dist
            
        # sprawdzamy wszystkich sasiadow
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            
            # upewniamy sie ze nie wychodzimy poza mape
            if 0 <= nr < rows and 0 <= nc < cols:
                # wchodzimy tylko tam gdzie nie ma sciany i gdzie jeszcze nie bylismy
                if G[nr][nc] != 'c' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, dist + 1))
                    
    # jak petla sie skonczy i nic nie znajdzie, to znaczy ze nie da sie dojsc
    return None

grid = [
    "s.c.",
    ".cc.",
    "...e"
]

# najpierw musimy znalezc kordynaty startowe dla naszego s
start_pos = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 's':
            start_pos = (i, j)
            break
    if start_pos:
        break

shortest_path = bfs_grid(grid, start_pos)