def has_pair_with_sum(arr, target_sum):
    """
    Check if there exists a pair of elements in the array that sum to the target value.
    
    Args:
        arr: List of integers
        target_sum: Target sum value
    
    Returns:
        bool: True if pair exists, False otherwise
    """
    seen = set()
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False

def find_pair_with_sum(arr, target_sum):
    """
    Find and return the first pair of elements that sum to the target value.
    
    Args:
        arr: List of integers
        target_sum: Target sum value
    
    Returns:
        tuple: Pair of numbers that sum to target, or None if no pair exists
    """
    seen = set()
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    
    return None

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 9),    # True: (4, 5)
        ([1, 2, 3, 4, 5], 10),   # False
        ([1, 2, 3, 4, 5], 7),    # True: (2, 5) or (3, 4)
        ([], 5),                 # False
        ([5], 5),                # False
        ([2, 4, 3, 5, 7], 9),   # True: (2, 7) or (4, 5)
    ]
    
    for arr, target in test_cases:
        result = has_pair_with_sum(arr, target)
        pair = find_pair_with_sum(arr, target)
        print(f"Array: {arr}, Target: {target}")
        print(f"Has pair: {result}, Pair: {pair}")
        print()