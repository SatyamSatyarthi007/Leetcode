#!/usr/bin/env python3
"""
Script to generate all remaining LeetCode problem solutions and README files.
This script creates solutions for problems 5-102 in the specified format.
"""

import os
import json

# Problem definitions with their solutions
problems = {
    # Array Problems (5-16)
    "05-maximum-subarray": {
        "title": "Maximum Subarray",
        "description": "Find the contiguous subarray with the largest sum.",
        "solution": """def max_subarray(nums):
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_subarray_with_indices(nums):
    if not nums:
        return (0, -1, -1)
    
    max_sum = current_sum = nums[0]
    start = end = temp_start = 0
    
    for i in range(1, len(nums)):
        if current_sum + nums[i] < nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return (max_sum, start, end)"""
    },
    
    "06-maximum-product-subarray": {
        "title": "Maximum Product Subarray",
        "description": "Find the contiguous subarray with the largest product.",
        "solution": """def max_product(nums):
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        
        result = max(result, max_prod)
    
    return result"""
    },
    
    "07-find-minimum-rotated-sorted-array": {
        "title": "Find Minimum in Rotated Sorted Array",
        "description": "Find the minimum element in a rotated sorted array.",
        "solution": """def find_min(nums):
    if not nums:
        return None
    
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]"""
    },
    
    "08-search-rotated-sorted-array": {
        "title": "Search in Rotated Sorted Array",
        "description": "Search for a target value in a rotated sorted array.",
        "solution": """def search(nums, target):
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1"""
    },
    
    "09-three-sum": {
        "title": "3 Sum",
        "description": "Find all unique triplets that sum to zero.",
        "solution": """def three_sum(nums):
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
    
    return result"""
    },
    
    "10-container-with-most-water": {
        "title": "Container With Most Water",
        "description": "Find two lines that form a container with maximum water.",
        "solution": """def max_area(height):
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
    
    return max_area"""
    },
    
    "11-factorial-large-number": {
        "title": "Factorial of Large Number",
        "description": "Calculate factorial of a large number.",
        "solution": """def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

def factorial_large(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return "1"
    
    result = [1]  # Store digits in reverse order
    
    for i in range(2, n + 1):
        carry = 0
        for j in range(len(result)):
            product = result[j] * i + carry
            result[j] = product % 10
            carry = product // 10
        
        while carry > 0:
            result.append(carry % 10)
            carry //= 10
    
    return ''.join(map(str, reversed(result)))"""
    },
    
    "12-trapping-rain-water": {
        "title": "Trapping Rain Water",
        "description": "Calculate trapped water between bars after raining.",
        "solution": """def trap(height):
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
    
    return trapped"""
    },
    
    "13-chocolate-distribution": {
        "title": "Chocolate Distribution Problem",
        "description": "Minimize difference between maximum and minimum chocolates distributed.",
        "solution": """def chocolate_distribution(arr, m):
    if not arr or m > len(arr) or m <= 0:
        return -1
    
    arr.sort()
    min_diff = float('inf')
    
    for i in range(len(arr) - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)
    
    return min_diff"""
    },
    
    "14-insert-interval": {
        "title": "Insert Interval",
        "description": "Insert a new interval into a list of non-overlapping intervals.",
        "solution": """def insert(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)
    
    # Add all intervals that come before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    result.append(new_interval)
    
    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result"""
    },
    
    "15-merge-intervals": {
        "title": "Merge Intervals",
        "description": "Merge all overlapping intervals.",
        "solution": """def merge(intervals):
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
    
    return result"""
    },
    
    "16-non-overlapping-intervals": {
        "title": "Non-overlapping Intervals",
        "description": "Find minimum number of intervals to remove to make rest non-overlapping.",
        "solution": """def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]
    
    return len(intervals) - count"""
    }
}

def create_solution_file(folder_name, problem_data):
    """Create solution.py file for a problem."""
    solution_content = f'''"""
{problem_data['title']}

{problem_data['description']}
"""

{problem_data['solution']}

if __name__ == "__main__":
    # Test cases
    print("Testing {problem_data['title']}")
    print("=" * 50)
    
    # Add specific test cases based on the problem
    # This is a template - customize for each specific problem
    test_cases = [
        # Add test cases here
    ]
    
    for test_case in test_cases:
        print(f"Input: {{test_case}}")
        # Add function call and output
        print()'''
    
    file_path = f"c:\\Users\\SATYAM\\Desktop\\leetcode\\{folder_name}\\solution.py"
    try:
        with open(file_path, 'w') as f:
            f.write(solution_content)
        print(f"Created solution file: {file_path}")
    except Exception as e:
        print(f"Error creating solution file {file_path}: {e}")

def create_readme_file(folder_name, problem_data):
    """Create README.md file for a problem."""
    readme_content = f"""# {problem_data['title']}

## Problem Description
{problem_data['description']}

## Examples
```
# Add specific examples for this problem
```

## Solution Approach
# Add specific approach for this problem

## Time Complexity
- **Time Complexity**: O(n) or as appropriate
- **Space Complexity**: O(1) or as appropriate

## Implementation Details
# Add specific implementation details

## Edge Cases
# Add edge cases specific to this problem"""
    
    file_path = f"c:\\Users\\SATYAM\\Desktop\\leetcode\\{folder_name}\\README.md"
    try:
        with open(file_path, 'w') as f:
            f.write(readme_content)
        print(f"Created README file: {file_path}")
    except Exception as e:
        print(f"Error creating README file {file_path}: {e}")

def main():
    """Generate all remaining problem solutions."""
    print("Generating remaining Array problem solutions...")
    
    for folder_name, problem_data in problems.items():
        create_solution_file(folder_name, problem_data)
        create_readme_file(folder_name, problem_data)
    
    print("\\nArray problems generation complete!")
    print("Next steps: Generate Matrix, String, Linked List, and other category problems...")

if __name__ == "__main__":
    main()