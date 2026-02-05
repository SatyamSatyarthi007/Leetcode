"""
XOR of All Subsets

Find XOR of all subsets of given array.
"""

def subset_xor_sum(nums):
    total_xor = 0
    n = len(nums)
    
    # Generate all subsets
    for mask in range(1 << n):
        current_xor = 0
        for i in range(n):
            if mask & (1 << i):
                current_xor ^= nums[i]
        total_xor += current_xor
    
    return total_xor

if __name__ == "__main__":
    print("Testing XOR of All Subsets")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")