"""
Count Decodings

Count ways to decode digit string to letters (A=1, B=2, etc.).
"""

def num_decodings(s):
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        # Single digit decode
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        
        # Two digit decode
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    
    return dp[n]

if __name__ == "__main__":
    print("Testing Count Decodings")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")