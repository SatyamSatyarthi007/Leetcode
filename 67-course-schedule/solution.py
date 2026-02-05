"""
Course Schedule

Check if all courses can be completed given prerequisites.
"""

def can_finish(num_courses, prerequisites):
    # Build adjacency list
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Find all courses with no prerequisites
    queue = [i for i in range(num_courses) if in_degree[i] == 0]
    completed = 0
    
    while queue:
        current = queue.pop(0)
        completed += 1
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return completed == num_courses

if __name__ == "__main__":
    print("Testing Course Schedule")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")