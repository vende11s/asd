'''
O(V+E)
'''

def topological_sort_dfs(graph, num_nodes):
    visited = [False] * num_nodes
    topo_order = []
    
    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)

        topo_order.append(u)

    for i in range(num_nodes):
        if not visited[i]:
            dfs(i)

    return topo_order[::-1]