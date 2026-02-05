def max_profit(prices):
    """
    Find maximum profit from buying and selling stock once.
    
    Args:
        prices: List of integers representing stock prices
    
    Returns:
        int: Maximum profit possible, or 0 if no profit can be made
    """
    if not prices or len(prices) < 2:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        # Update minimum price seen so far
        if price < min_price:
            min_price = price
        # Calculate profit if we sell at current price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    
    return max_profit

def max_profit_with_days(prices):
    """
    Find maximum profit and the buy/sell days.
    
    Args:
        prices: List of integers representing stock prices
    
    Returns:
        tuple: (max_profit, buy_day, sell_day) or (0, -1, -1) if no profit
    """
    if not prices or len(prices) < 2:
        return (0, -1, -1)
    
    min_price = prices[0]
    min_day = 0
    max_profit = 0
    buy_day = sell_day = -1
    
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i
        else:
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit
                buy_day = min_day
                sell_day = i
    
    return (max_profit, buy_day, sell_day)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [7, 1, 5, 3, 6, 4],    # Expected: 5 (buy at 1, sell at 6)
        [7, 6, 4, 3, 1],       # Expected: 0 (prices only decrease)
        [1, 2],                # Expected: 1 (buy at 1, sell at 2)
        [2, 1],                # Expected: 0 (loss)
        [1, 1, 1, 1],          # Expected: 0 (no profit)
        [],                    # Expected: 0 (empty array)
    ]
    
    for prices in test_cases:
        profit = max_profit(prices)
        profit_with_days = max_profit_with_days(prices)
        print(f"Prices: {prices}")
        print(f"Max profit: {profit}")
        print(f"Max profit with days: {profit_with_days}")
        print()