def product_except_self(nums):
    """
    Calculate product of array except self without using division.
    
    Args:
        nums: List of integers
    
    Returns:
        list: Product array where result[i] = product of all elements except nums[i]
    """
    n = len(nums)
    if n == 0:
        return []
    
    # Initialize result array
    result = [1] * n
    
    # Left products: product of all elements to the left of i
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Right products: product of all elements to the right of i
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

def product_except_self_with_division(nums):
    """
    Calculate product of array except self using division.
    Note: This approach fails when there are zeros in the array.
    
    Args:
        nums: List of integers
    
    Returns:
        list: Product array
    """
    n = len(nums)
    if n == 0:
        return []
    
    total_product = 1
    for num in nums:
        total_product *= num
    
    result = []
    for num in nums:
        if num != 0:
            result.append(total_product // num)
        else:
            # Handle division by zero
            result.append(0)
    
    return result

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [1, 0, 3, 4],
        [0, 0, 0, 0],
        [1],
        [-1, 2, -3, 4],
    ]
    
    for nums in test_cases:
        result = product_except_self(nums)
        print(f"Input: {nums}")
        print(f"Product except self: {result}")
        
        # Verify result
        expected = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            expected.append(product)
        
        print(f"Expected: {expected}")
        print(f"Correct: {result == expected}")
        print()