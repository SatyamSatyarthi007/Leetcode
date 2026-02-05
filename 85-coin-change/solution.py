"""
Coin Change

Find minimum number of coins to make given amount.
"""

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    print("Testing Coin Change")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")