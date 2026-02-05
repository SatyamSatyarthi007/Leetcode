"""
Maximum Product Cutting

Find maximum product by cutting rope of given length.
"""

def max_product_cutting(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    
    for i in range(4, n + 1):
        max_product = 0
        for j in range(1, i // 2 + 1):
            max_product = max(max_product, dp[j] * dp[i - j])
        dp[i] = max_product
    
    return dp[n]

if __name__ == "__main__":
    print("Testing Maximum Product Cutting")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")