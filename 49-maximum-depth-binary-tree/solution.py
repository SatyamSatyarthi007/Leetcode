"""
Maximum Depth of Binary Tree

Find maximum depth of binary tree.
"""

def max_depth(root):
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1

if __name__ == "__main__":
    print("Testing Maximum Depth of Binary Tree")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")