# Check if Pair with Given Sum Exists in Array

## Problem Description
Given an array of integers and a target sum, determine if there exists any pair of elements in the array that sum up to the target value.

## Examples
```
Input: arr = [1, 2, 3, 4, 5], target_sum = 9
Output: True
Explanation: Pair (4, 5) sums to 9

Input: arr = [1, 2, 3, 4, 5], target_sum = 10
Output: False
Explanation: No pair sums to 10
```

## Solution Approach
1. **Hash Set Approach**: Use a set to store seen elements
2. For each element, check if its complement (target_sum - current_element) exists in the set
3. If found, return True; otherwise add current element to set and continue

## Time Complexity
- **Time Complexity**: O(n) where n is the length of the array
- **Space Complexity**: O(n) for the hash set

## Implementation Details
The solution includes two functions:
- `has_pair_with_sum()`: Returns boolean indicating if pair exists
- `find_pair_with_sum()`: Returns the actual pair if found

## Test Cases
- Normal cases with existing pairs
- Edge cases: empty array, single element
- Cases with no valid pairs