'''
zwraca najkrotsze sciezki ze startu do kazdego z wierzcholkow
'''

from queue import PriorityQueue

'''
G = [
# 0 [(1,3), (2, 5) ...] # (wierzcholek, waga)
# 1 ...
...]
'''


def dijkstra(G, start):
    distances = [float('inf') for _ in range(len(G))]
    distances[start] = 0

    Q = PriorityQueue()
    Q.put((0, start))

    while not Q.empty():
        dist, v = Q.get()

        for n in G[v]:
            dist_n = dist + n[1]
            if dist_n > distances[n]:
                continue
            distances[n] = dist_n
            Q.put((dist_n, n)) 

    return distances

