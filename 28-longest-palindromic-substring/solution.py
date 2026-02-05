"""
Longest Palindromic Substring

Find longest palindromic substring in a string.
"""

def longest_palindrome(s):
    if not s:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    
    for i in range(len(s)):
        # Odd length palindrome
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Even length palindrome
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest

if __name__ == "__main__":
    print("Testing Longest Palindromic Substring")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")