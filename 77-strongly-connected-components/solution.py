"""
Strongly Connected Components

Find strongly connected components using Kosaraju's algorithm.
"""

def find_scc(graph):
    n = len(graph)
    visited = [False] * n
    stack = []
    
    # First pass: fill stack with finishing times
    def dfs1(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(node)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
    
    # Reverse graph
    reverse_graph = [[] for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            reverse_graph[j].append(i)
    
    # Second pass: find SCCs
    visited = [False] * n
    sccs = []
    
    def dfs2(node, current_scc):
        visited[node] = True
        current_scc.append(node)
        for neighbor in reverse_graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor, current_scc)
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            current_scc = []
            dfs2(node, current_scc)
            sccs.append(current_scc)
    
    return sccs

if __name__ == "__main__":
    print("Testing Strongly Connected Components")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")