"""
Next Greater Element

Find next greater element for each element in array.
"""

def next_greater_elements(nums):
    result = [-1] * len(nums)
    stack = []
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    
    return result

if __name__ == "__main__":
    print("Testing Next Greater Element")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")