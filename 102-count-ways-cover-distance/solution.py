"""
Count Ways to Cover Distance

Count ways to cover distance of n meters using 1, 2, or 3 meter steps.
"""

def count_ways(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[n]

if __name__ == "__main__":
    print("Testing Count Ways to Cover Distance")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")