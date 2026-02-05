"""
Longest Increasing Subsequence

Find length of longest increasing subsequence.
"""

def length_of_lis(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

if __name__ == "__main__":
    print("Testing Longest Increasing Subsequence")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")