"""
Check if Graph is Bipartite

Check if graph can be colored with 2 colors (bipartite).
"""

def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n
    
    def bfs(start):
        queue = [start]
        color[start] = 0
        
        while queue:
            node = queue.pop(0)
            
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                return False
    
    return True

if __name__ == "__main__":
    print("Testing Check if Graph is Bipartite")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")