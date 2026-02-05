"""
Construct Binary Tree from Preorder and Inorder

Construct binary tree from preorder and inorder traversal.
"""

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    root_index = inorder.index(preorder[0])
    
    root.left = build_tree(preorder[1:root_index + 1], inorder[:root_index])
    root.right = build_tree(preorder[root_index + 1:], inorder[root_index + 1:])
    
    return root

if __name__ == "__main__":
    print("Testing Construct Binary Tree from Preorder and Inorder")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")