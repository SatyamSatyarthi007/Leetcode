"""
Bridges in Graph

Find all bridges in undirected graph using Tarjan's algorithm.
"""

def find_bridges(graph):
    n = len(graph)
    discovery = [-1] * n
    low = [-1] * n
    bridges = []
    time = 0
    
    def dfs(u, parent):
        nonlocal time
        discovery[u] = low[u] = time
        time += 1
        
        for v in graph[u]:
            if discovery[v] == -1:  # Not visited
                dfs(v, u)
                low[u] = min(low[u], low[v])
                
                # Bridge condition
                if low[v] > discovery[u]:
                    bridges.append([u, v])
            elif v != parent:  # Back edge
                low[u] = min(low[u], discovery[v])
    
    for i in range(n):
        if discovery[i] == -1:
            dfs(i, -1)
    
    return bridges

if __name__ == "__main__":
    print("Testing Bridges in Graph")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")