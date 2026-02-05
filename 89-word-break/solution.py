"""
Word Break

Check if string can be segmented into dictionary words.
"""

def word_break(s, word_dict):
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[len(s)]

if __name__ == "__main__":
    print("Testing Word Break")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")