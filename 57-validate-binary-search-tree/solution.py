"""
Validate Binary Search Tree

Check if binary tree is valid BST.
"""

def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    print("Testing Validate Binary Search Tree")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")