"""
Pacific Atlantic Water Flow

Find cells where water can flow to both Pacific and Atlantic.
"""

def pacific_atlantic(matrix):
    if not matrix or not matrix[0]:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    pacific_reachable = [[False] * cols for _ in range(rows)]
    atlantic_reachable = [[False] * cols for _ in range(rows)]
    
    def dfs(i, j, reachable):
        reachable[i][j] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (0 <= ni < rows and 0 <= nj < cols and 
                not reachable[ni][nj] and 
                matrix[ni][nj] >= matrix[i][j]):
                dfs(ni, nj, reachable)
    
    # Start DFS from borders
    for i in range(rows):
        dfs(i, 0, pacific_reachable)
        dfs(i, cols - 1, atlantic_reachable)
    
    for j in range(cols):
        dfs(0, j, pacific_reachable)
        dfs(rows - 1, j, atlantic_reachable)
    
    # Find cells reachable from both
    result = []
    for i in range(rows):
        for j in range(cols):
            if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                result.append([i, j])
    
    return result

if __name__ == "__main__":
    print("Testing Pacific Atlantic Water Flow")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")