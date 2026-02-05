"""
Find Minimum in Rotated Sorted Array

Find the minimum element in a rotated sorted array.
"""

def find_min(nums):
    if not nums:
        return None
    
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]

if __name__ == "__main__":
    # Test cases
    print("Testing Find Minimum in Rotated Sorted Array")
    print("=" * 50)
    
    # Add specific test cases based on the problem
    # This is a template - customize for each specific problem
    test_cases = [
        # Add test cases here
    ]
    
    for test_case in test_cases:
        print(f"Input: {test_case}")
        # Add function call and output
        print()