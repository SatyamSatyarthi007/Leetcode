"""
Chocolate Distribution Problem

Minimize difference between maximum and minimum chocolates distributed.
"""

def chocolate_distribution(arr, m):
    if not arr or m > len(arr) or m <= 0:
        return -1
    
    arr.sort()
    min_diff = float('inf')
    
    for i in range(len(arr) - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)
    
    return min_diff

if __name__ == "__main__":
    # Test cases
    print("Testing Chocolate Distribution Problem")
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