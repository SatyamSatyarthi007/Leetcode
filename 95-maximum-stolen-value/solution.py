"""
Maximum Stolen Value

Find maximum value that can be stolen without stealing adjacent houses.
"""

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp[-1]

if __name__ == "__main__":
    print("Testing Maximum Stolen Value")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")