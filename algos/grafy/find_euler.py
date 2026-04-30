def euler(G):
    n = len(G)
    idx = [0 for _ in range(n)]
    cycle = []
    def dfs_visit(v):
        nonlocal G, idx, cycle
        while idx[v]<len(G[v]):
            u = G[v][idx[v]]
            idx[v]+=1
            if idx[u]>=len(G[u]) or G[u][idx[u]]>v:
                continue
            dfs_visit(u)
        cycle.append(v)
    dfs_visit(0)
    return cycle