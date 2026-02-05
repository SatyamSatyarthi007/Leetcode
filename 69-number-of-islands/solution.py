"""
Number of Islands

Count number of islands in 2D binary grid.
"""

def num_islands(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(i, j):
        if (i < 0 or i >= rows or j < 0 or j >= cols or 
            grid[i][j] == '0'):
            return
        
        grid[i][j] = '0'  # Mark as visited
        
        # Explore all 4 directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                islands += 1
                dfs(i, j)
    
    return islands

if __name__ == "__main__":
    print("Testing Number of Islands")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")