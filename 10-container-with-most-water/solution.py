"""
Container With Most Water

Find two lines that form a container with maximum water.
"""

def max_area(height):
    if not height or len(height) < 2:
        return 0
    
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_area = max(max_area, current_area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

if __name__ == "__main__":
    # Test cases
    print("Testing Container With Most Water")
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