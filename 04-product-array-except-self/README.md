# Product of Array Except Self

## Problem Description
Given an array of integers, return an array where each element at index i is the product of all elements in the original array except the element at index i.

**Constraint**: Solve without using division and in O(n) time.

## Examples
```
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Explanation: 
- result[0] = 2 * 3 * 4 = 24
- result[1] = 1 * 3 * 4 = 12
- result[2] = 1 * 2 * 4 = 8
- result[3] = 1 * 2 * 3 = 6

Input: nums = [2, 3, 4, 5]
Output: [60, 40, 30, 24]
```

## Solution Approach
1. **Two Pass Algorithm**: Use left and right product arrays
2. First pass: Calculate products of all elements to the left of each index
3. Second pass: Calculate products of all elements to the right of each index
4. Multiply left and right products for final result

## Time Complexity
- **Time Complexity**: O(n) where n is the length of the array
- **Space Complexity**: O(1) excluding the output array (O(n) including output)

## Implementation Details
- `product_except_self()`: Main solution without division
- `product_except_self_with_division()`: Alternative approach (has limitations with zeros)

## Edge Cases
- Array with zeros
- Single element array
- Array with negative numbers
- All zeros array