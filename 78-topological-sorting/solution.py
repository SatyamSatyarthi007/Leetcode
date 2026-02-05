"""
Topological Sorting

Perform topological sort on directed acyclic graph.
"""

def topological_sort(graph):
    n = len(graph)
    in_degree = [0] * n
    
    # Calculate in-degrees
    for i in range(n):
        for j in graph[i]:
            in_degree[j] += 1
    
    # Find all nodes with no incoming edges
    queue = [i for i in range(n) if in_degree[i] == 0]
    result = []
    
    while queue:
        node = queue.pop(0)
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == n else []  # Empty if cycle exists

if __name__ == "__main__":
    print("Testing Topological Sorting")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")