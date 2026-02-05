"""
Infix to Postfix Conversion

Convert infix expression to postfix notation.
"""

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []
    
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while (stack and stack[-1] != '(' and 
                   precedence.get(stack[-1], 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

if __name__ == "__main__":
    print("Testing Infix to Postfix Conversion")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")