"""
Unique Paths with Obstacles

Find number of unique paths in grid with obstacles.
"""

def unique_paths_with_obstacles(obstacle_grid):
    if not obstacle_grid or obstacle_grid[0][0] == 1:
        return 0
    
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    
    # Fill first row
    for j in range(1, n):
        if obstacle_grid[0][j] == 0:
            dp[0][j] = dp[0][j - 1]
    
    # Fill first column
    for i in range(1, m):
        if obstacle_grid[i][0] == 0:
            dp[i][0] = dp[i - 1][0]
    
    # Fill rest of grid
    for i in range(1, m):
        for j in range(1, n):
            if obstacle_grid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]

if __name__ == "__main__":
    print("Testing Unique Paths with Obstacles")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")