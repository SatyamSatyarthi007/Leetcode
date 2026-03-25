def find_duplicates(arr):
    """
    Find all duplicate elements in the array.
    
    Args:
        arr: List of integers
    
    Returns:
        list: List of duplicate elements
    """
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

def find_duplicates_with_count(arr):
    """
    Find all duplicate elements with their counts.
    
    Args:
        arr: List of integers
    
    Returns:
        dict: Dictionary with duplicate elements as keys and their counts as values
    """
    count = {}
    
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    # Filter only duplicates (count > 1)
    duplicates = {num: cnt for num, cnt in count.items() if cnt > 1}
    
    return duplicates

def find_all_duplicates(arr):
    """
    Find all occurrences of duplicate elements.
    
    Args:
        arr: List of integers
    
    Returns:
        list: List of all duplicate elements (including multiple occurrences)
    """
    count = {}
    result = []
    
    for num in arr:
        count[num] = count.get(num, 0) + 1
        if count[num] > 1:
            result.append(num)
    
    return result

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 2, 5, 6, 3, 7],
        [1, 2, 3, 4, 5],
        [1, 1, 1, 1, 1],
        [5, 5, 5, 2, 2, 3],
        [],
        [1],
    ]
    
    for arr in test_cases:
        duplicates = find_duplicates(arr)
        duplicates_with_count = find_duplicates_with_count(arr)
        all_duplicates = find_all_duplicates(arr)
        
        print(f"Array: {arr}")
        print(f"Unique duplicates: {duplicates}")
        print(f"Duplicates with count: {duplicates_with_count}")
        print(f"All duplicate occurrences: {all_duplicates}")
        print()