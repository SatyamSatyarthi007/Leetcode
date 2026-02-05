"""
Egg Dropping Problem

Find minimum trials needed to find critical floor with k eggs and n floors.
"""

def egg_drop(k, n):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base cases
    for i in range(1, n + 1):
        dp[i][1] = i  # 1 egg case
    
    for j in range(1, k + 1):
        dp[1][j] = 1  # 1 floor case
    
    # Fill dp table
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = float('inf')
            for x in range(1, i + 1):
                # Egg breaks or doesn't break
                worst_case = 1 + max(dp[x - 1][j - 1], dp[i - x][j])
                dp[i][j] = min(dp[i][j], worst_case)
    
    return dp[n][k]

if __name__ == "__main__":
    print("Testing Egg Dropping Problem")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")