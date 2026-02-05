"""
Count Ways to Reach Nth Stair

Count ways to reach nth stair taking 1 or 2 steps at a time.
"""

def climb_stairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

if __name__ == "__main__":
    print("Testing Count Ways to Reach Nth Stair")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")