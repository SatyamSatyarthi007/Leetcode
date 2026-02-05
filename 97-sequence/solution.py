"""
Sequence Pattern Matching

Check if string S is subsequence of string T.
"""

def is_subsequence(s, t):
    i = j = 0
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return i == len(s)

if __name__ == "__main__":
    print("Testing Sequence Pattern Matching")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")