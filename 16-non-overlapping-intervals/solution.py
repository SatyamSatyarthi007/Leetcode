"""
Non-overlapping Intervals

Find minimum number of intervals to remove to make rest non-overlapping.
"""

def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]
    
    return len(intervals) - count

if __name__ == "__main__":
    # Test cases
    print("Testing Non-overlapping Intervals")
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