"""
Cutting Rod Problem

Find maximum value obtainable by cutting rod of given length.
"""

def cut_rod(price, n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            max_val = max(max_val, price[j] + dp[i - j - 1])
        dp[i] = max_val
    
    return dp[n]

if __name__ == "__main__":
    print("Testing Cutting Rod Problem")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")