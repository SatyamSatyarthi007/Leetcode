"""
0/1 Knapsack Problem

Solve 0/1 knapsack problem with given weights and values.
"""

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], 
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

if __name__ == "__main__":
    print("Testing 0/1 Knapsack Problem")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")