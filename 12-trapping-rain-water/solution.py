"""
Trapping Rain Water

Calculate trapped water between bars after raining.
"""

def trap(height):
    if not height or len(height) < 3:
        return 0
    
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    
    # Fill left_max array
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # Fill right_max array
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # Calculate trapped water
    trapped = 0
    for i in range(n):
        trapped += max(0, min(left_max[i], right_max[i]) - height[i])
    
    return trapped

if __name__ == "__main__":
    # Test cases
    print("Testing Trapping Rain Water")
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