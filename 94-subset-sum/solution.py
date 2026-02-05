"""
Subset Sum Problem

Check if subset with given sum exists.
"""

def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Base case: sum 0 is always possible
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][target]

if __name__ == "__main__":
    print("Testing Subset Sum Problem")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")