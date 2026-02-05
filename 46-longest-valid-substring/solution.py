"""
Longest Valid Substring of Parentheses

Find longest valid substring of well-formed parentheses.
"""

def longest_valid_parentheses(s):
    stack = [-1]  # Base for valid substring calculation
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # New base
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length

if __name__ == "__main__":
    print("Testing Longest Valid Substring of Parentheses")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")