"""
Factorial of Large Number

Calculate factorial of a large number.
"""

def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

def factorial_large(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return "1"
    
    result = [1]  # Store digits in reverse order
    
    for i in range(2, n + 1):
        carry = 0
        for j in range(len(result)):
            product = result[j] * i + carry
            result[j] = product % 10
            carry = product // 10
        
        while carry > 0:
            result.append(carry % 10)
            carry //= 10
    
    return ''.join(map(str, reversed(result)))

if __name__ == "__main__":
    # Test cases
    print("Testing Factorial of Large Number")
    print("=" * 50)
    
    # Add specific test cases based on the problem
    # This is a template - customize for each specific problem
    test_cases = [
        # Add test cases here
    ]
    
    for test_case in test_cases:
        print(f"Input: {test_case}")
        # Add function call and output
        print()