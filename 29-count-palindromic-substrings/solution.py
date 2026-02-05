"""
Count Palindromic Substrings

Count all palindromic substrings in a string.
"""

def count_substrings(s):
    if not s:
        return 0
    
    def count_palindromes_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    total_count = 0
    
    for i in range(len(s)):
        # Odd length palindromes
        total_count += count_palindromes_around_center(i, i)
        # Even length palindromes
        total_count += count_palindromes_around_center(i, i + 1)
    
    return total_count

if __name__ == "__main__":
    print("Testing Count Palindromic Substrings")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")