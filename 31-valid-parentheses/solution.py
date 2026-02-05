"""
Valid Parentheses

Check if parentheses are valid and properly nested.
"""

def is_valid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

if __name__ == "__main__":
    print("Testing Valid Parentheses")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")