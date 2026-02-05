"""
Check Anagram

Check if two strings are anagrams of each other.
"""

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    return len(char_count) == 0

if __name__ == "__main__":
    print("Testing Check Anagram")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")