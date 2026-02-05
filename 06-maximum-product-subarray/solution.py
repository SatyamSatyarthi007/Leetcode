"""
Maximum Product Subarray

Find the contiguous subarray with the largest product.
"""

def max_product(nums):
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        
        result = max(result, max_prod)
    
    return result

if __name__ == "__main__":
    # Test cases
    print("Testing Maximum Product Subarray")
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