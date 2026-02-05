"""
Missing Number

Find missing number in array containing 0 to n.
"""

def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def missing_number_xor(nums):
    n = len(nums)
    result = n
    for i in range(n):
        result ^= i ^ nums[i]
    return result

if __name__ == "__main__":
    print("Testing Missing Number")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")