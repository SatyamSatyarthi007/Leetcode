"""
Celebrity Problem

Find celebrity in a group who is known by everyone but knows no one.
"""

def find_celebrity(matrix):
    n = len(matrix)
    stack = list(range(n))
    
    # Find potential celebrity
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        
        if matrix[a][b] == 1:  # a knows b, so a is not celebrity
            stack.append(b)
        else:  # a doesn't know b, so b is not celebrity
            stack.append(a)
    
    if not stack:
        return -1
    
    candidate = stack[0]
    
    # Verify candidate
    for i in range(n):
        if i != candidate and (matrix[candidate][i] == 1 or matrix[i][candidate] == 0):
            return -1
    
    return candidate

if __name__ == "__main__":
    print("Testing Celebrity Problem")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")