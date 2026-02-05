"""
Invert Binary Tree

Invert a binary tree (mirror image).
"""

def invert_tree(root):
    if not root:
        return None
    
    # Swap left and right subtrees
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root

if __name__ == "__main__":
    print("Testing Invert Binary Tree")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")