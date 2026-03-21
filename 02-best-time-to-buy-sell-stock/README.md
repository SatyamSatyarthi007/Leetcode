# Best Time to Buy and Sell Stock

## Problem Description
Given an array of stock prices where prices[i] is the price of a stock on day i, find the maximum profit you can achieve from one transaction (buy once and sell once). You must buy before you sell.

## Examples
```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5

Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: No transactions are done, max profit = 0
```

## Solution Approach
1. **Single Pass Algorithm**: Track minimum price seen so far and maximum profit
2. For each price, calculate profit if sold at current price (current_price - min_price)
3. Update maximum profit if current profit is higher

## Time Complexity
- **Time Complexity**: O(n) where n is the number of days
- **Space Complexity**: O(1) constant space

## Implementation Details
The solution includes:
- `max_profit()`: Returns maximum profit possible
- `max_profit_with_days()`: Returns profit along with buy/sell days

## Edge Cases
- Empty array or single element
- Prices in descending order (no profit possible)
- All prices equal (no profit possible)
- Minimum length array (2 elements)