"""
Dice Throw Problem

Find number of ways to get sum S with n dice each having m faces.
"""

def find_ways(m, n, target_sum):
    dp = [[0] * (target_sum + 1) for _ in range(n + 1)]
    
    # Base case: 1 die
    for j in range(1, min(m + 1, target_sum + 1)):
        dp[1][j] = 1
    
    # Fill dp table
    for i in range(2, n + 1):
        for j in range(1, target_sum + 1):
            for k in range(1, m + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
    
    return dp[n][target_sum]

if __name__ == "__main__":
    print("Testing Dice Throw Problem")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")