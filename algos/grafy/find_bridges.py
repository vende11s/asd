'''
O(V + E)
'''

def find_bridges(G):
    n = len(G)

    visited = [False] * n
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    bridges = []

    def dfs(v, parent=-1):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1

        for to in G[v]:
            if to == parent:
                continue
            
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                
                if low[to] > tin[v]:
                    bridges.append((v, to))

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return bridges