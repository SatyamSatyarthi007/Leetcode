"""
Delete Middle Element of Stack

Delete middle element from stack without using extra space.
"""

def delete_middle(stack, n, current=0):
    if not stack:
        return
    
    # Base case: when current equals middle element
    if current == n // 2:
        stack.pop()
        return
    
    # Remove current element
    temp = stack.pop()
    
    # Recursively remove middle from remaining stack
    delete_middle(stack, n, current + 1)
    
    # Put back the removed element
    stack.append(temp)

if __name__ == "__main__":
    print("Testing Delete Middle Element of Stack")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")