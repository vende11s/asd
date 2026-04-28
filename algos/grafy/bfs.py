'''
prosty bfs do znajdowania miedzy wierzcholkami w grafie bez wag
'''
from collections import deque

def BFS(G, start):
    distance = [-1 for _ in range(len(G))]
    distance[start] = 0

    Q = deque()
    Q.append((start, 0)) # w kolejce trzymamy nr wierzcholka i odleglosc do startu
    while Q:
        v, dist = Q.popleft()

        for neigbour in G[v]:
            if distance[neigbour] != -1: # jak już bylismy u tego sasiada
                continue                 # to krotszej drogi nie znajdziemy

            distance[neigbour] = dist+1
            Q.append((neigbour, dist + 1))
            
    return distance