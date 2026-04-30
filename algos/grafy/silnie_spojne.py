'''
O(V + E)
'''

def find_scc(n, edges):
    # G - normalny graf, GR - graf odwrócony
    G = [[] for _ in range(n)]
    GR = [[] for _ in range(n)]
    
    for u, v in edges:
        G[u].append(v)
        GR[v].append(u) 
        
    visited = [False] * n
    order = []
    
    def dfs1(v):
        visited[v] = True
        for to in G[v]:
            if not visited[to]:
                dfs1(to)
        order.append(v)
        
    for i in range(n):
        if not visited[i]:
            dfs1(i)
            
    visited = [False] * n
    scc_list = []
    
    def dfs2(v, current_scc):
        visited[v] = True
        current_scc.append(v)
        for to in GR[v]:
            if not visited[to]:
                dfs2(to, current_scc)
                
    for i in reversed(order):
        if not visited[i]:
            current_scc = []
            dfs2(i, current_scc)
            scc_list.append(current_scc)
            
    return scc_list
