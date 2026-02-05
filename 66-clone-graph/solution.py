"""
Clone Graph

Clone an undirected graph with all nodes and edges.
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    if not node:
        return None
    
    visited = {}
    
    def dfs(original):
        if original in visited:
            return visited[original]
        
        clone = Node(original.val)
        visited[original] = clone
        
        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)

if __name__ == "__main__":
    print("Testing Clone Graph")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")