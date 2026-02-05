"""
Longest Consecutive Sequence

Find longest consecutive sequence in unsorted array.
"""

def longest_consecutive(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current = num
            current_length = 1
            
            while current + 1 in num_set:
                current += 1
                current_length += 1
            
            longest = max(longest, current_length)
    
    return longest

if __name__ == "__main__":
    print("Testing Longest Consecutive Sequence")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")