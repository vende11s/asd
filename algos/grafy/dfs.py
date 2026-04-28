from collections import deque

def dfs(G, start):
    visited = [False for _ in range(len(G))]

    Q = deque()
    visited[start] = True

    Q.append(start)
    while Q:
        v = Q.pop()

        for neighbour in G[v]:
            if visited[neighbour]:
                continue
            
            visited[neighbour] = True
            Q.append(neighbour)
            
    return visited