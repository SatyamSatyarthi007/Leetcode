"""
Merge Intervals

Merge all overlapping intervals.
"""

def merge(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    
    for i in range(1, len(intervals)):
        current = intervals[i]
        last = result[-1]
        
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            result.append(current)
    
    return result

if __name__ == "__main__":
    # Test cases
    print("Testing Merge Intervals")
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