"""
Smallest Window Containing Substring

Find smallest window in string containing all characters of another string.
"""

def min_window(s, t):
    from collections import Counter
    
    if not s or not t:
        return ""
    
    t_count = Counter(t)
    required = len(t_count)
    formed = 0
    
    window_count = {}
    left = 0
    min_length = float('inf')
    min_left = 0
    
    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        while formed == required and left <= right:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left = left
            
            left_char = s[left]
            window_count[left_char] -= 1
            if left_char in t_count and window_count[left_char] < t_count[left_char]:
                formed -= 1
            left += 1
    
    return "" if min_length == float('inf') else s[min_left:min_left + min_length]

if __name__ == "__main__":
    print("Testing Smallest Window Containing Substring")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")