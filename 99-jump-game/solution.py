"""
Jump Game

Check if you can reach last index from first index.
"""

def can_jump(nums):
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) - 1:
            return True
    
    return True

if __name__ == "__main__":
    print("Testing Jump Game")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")