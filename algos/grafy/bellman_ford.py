'''
O(VE)
'''

def bellman_ford(E, start, n):
    distances = [float('inf') for _ in range(n)]
    distances[start] = 0
    
    for _ in range(n - 1):
        any_update = False
        for edge in E:
            u, v, cost = edge
            if distances[u] != float('inf') and distances[u] + cost < distances[v]:
                distances[v] = distances[u] + cost
                any_update = True
                
        if not any_update:
            break

    # Wykrywanie ujemnych cykli 
    for edge in E:
        u, v, cost = edge
        if distances[u] != float('inf') and distances[u] + cost < distances[v]:
            return float('-inf')

    return distances