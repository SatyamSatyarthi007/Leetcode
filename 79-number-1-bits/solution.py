"""
Number of 1 Bits

Count number of 1 bits in binary representation.
"""

def hamming_weight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def hamming_weight_alternative(n):
    count = 0
    while n:
        n &= n - 1  # Remove rightmost 1
        count += 1
    return count

if __name__ == "__main__":
    print("Testing Number of 1 Bits")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")