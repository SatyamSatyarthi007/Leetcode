"""
Counting Bits

Count number of 1 bits for all numbers from 0 to n.
"""

def count_bits(n):
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)
    
    return result

if __name__ == "__main__":
    print("Testing Counting Bits")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")