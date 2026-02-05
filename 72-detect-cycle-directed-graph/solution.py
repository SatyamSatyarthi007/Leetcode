"""
Detect Cycle in Directed Graph

Detect if directed graph contains cycle using DFS.
"""

def has_cycle(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * len(graph)
    
    def dfs(node):
        if color[node] == GRAY:
            return True  # Cycle detected
        if color[node] == BLACK:
            return False  # Already processed
        
        color[node] = GRAY
        
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        
        color[node] = BLACK
        return False
    
    for i in range(len(graph)):
        if color[i] == WHITE:
            if dfs(i):
                return True
    
    return False

if __name__ == "__main__":
    print("Testing Detect Cycle in Directed Graph")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")