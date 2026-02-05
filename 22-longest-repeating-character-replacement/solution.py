"""
Longest Repeating Character Replacement

Find longest substring with repeating characters after at most k replacements.
"""

def character_replacement(s, k):
    if not s:
        return 0
    
    char_count = {}
    max_count = max_length = 0
    left = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_count = max(max_count, char_count[s[right]])
        
        # If current window size - max_count > k, shrink window
        if (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

if __name__ == "__main__":
    print("Testing Longest Repeating Character Replacement")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")