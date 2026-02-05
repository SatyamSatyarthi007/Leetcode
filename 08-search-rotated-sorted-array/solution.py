"""
Search in Rotated Sorted Array

Search for a target value in a rotated sorted array.
"""

def search(nums, target):
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

if __name__ == "__main__":
    # Test cases
    print("Testing Search in Rotated Sorted Array")
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