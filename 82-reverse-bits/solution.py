"""
Reverse Bits

Reverse bits of a 32-bit unsigned integer.
"""

def reverse_bits(n):
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

if __name__ == "__main__":
    print("Testing Reverse Bits")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")