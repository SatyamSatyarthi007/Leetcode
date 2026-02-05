"""
Lowest Common Ancestor of BST

Find lowest common ancestor of two nodes in BST.
"""

def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    
    # Both nodes are in left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # Both nodes are in right subtree
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # Current node is LCA
    return root

if __name__ == "__main__":
    print("Testing Lowest Common Ancestor of BST")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")