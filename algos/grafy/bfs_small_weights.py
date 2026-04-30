'''
mamy znalezc najkrotsza sciezke w grafie wazonym, ale wagi są mniejsze od np. 10

nie oplaca sie zlozonosciowo robic djikstry bo mozna zrobic bfsa
'''

from collections import deque

def BFS(G, start):
    distance = [float('inf') for _ in range(len(G))]
    distance[start] = 0

    Q = deque()
    # W kolejce trzymamy: (nr wierzcholka, odleglosc do startu, pozostaly czas)
    Q.append((start, 0, 0)) 
    
    while Q:
        v, dist, left = Q.popleft()
        
        # 1. Odliczanie czasu (symulacja wagi)
        if left != 0:
            left -= 1
            Q.append((v, dist, left))
            continue

        # 2. Odcinanie martwych stanów (optymalizacja)
        if dist > distance[v]:
            continue

        # 3. Przeglądanie sąsiadów
        for neigbour, w in G[v]:
            if distance[neigbour] > dist + w:
                distance[neigbour] = dist + w
                # KLUCZOWA ZMIANA: w - 1
                Q.append((neigbour, dist + w, w - 1))

    return distance