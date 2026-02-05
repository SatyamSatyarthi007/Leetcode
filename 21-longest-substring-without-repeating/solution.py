"""
Longest Substring Without Repeating Characters

Find length of longest substring without repeating characters.
"""

def length_of_longest_substring(s):
    if not s:
        return 0
    
    char_index = {}
    max_length = start = 0
    
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    
    return max_length

if __name__ == "__main__":
    print("Testing Longest Substring Without Repeating Characters")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")