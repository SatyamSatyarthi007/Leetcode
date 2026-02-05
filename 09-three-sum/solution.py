"""
3 Sum

Find all unique triplets that sum to zero.
"""

def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

if __name__ == "__main__":
    # Test cases
    print("Testing 3 Sum")
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