# Find Duplicates in Array

## Problem Description
Given an array of integers, find all duplicate elements in the array.

## Examples
```
Input: arr = [1, 2, 3, 4, 2, 5, 6, 3, 7]
Output: [2, 3]
Explanation: Elements 2 and 3 appear more than once

Input: arr = [1, 2, 3, 4, 5]
Output: []
Explanation: No duplicates found
```

## Solution Approach
1. **Hash Set Approach**: Use a set to track seen elements and another set for duplicates
2. **Counting Approach**: Use a dictionary to count occurrences of each element

## Time Complexity
- **Time Complexity**: O(n) where n is the length of the array
- **Space Complexity**: O(n) for the hash set/dictionary

## Implementation Details
The solution includes three functions:
- `find_duplicates()`: Returns unique duplicate elements
- `find_duplicates_with_count()`: Returns duplicates with their counts
- `find_all_duplicates()`: Returns all occurrences of duplicate elements

## Variations
- Find unique duplicates only
- Find duplicates with their frequency
- Find all duplicate occurrences (including multiple instances)