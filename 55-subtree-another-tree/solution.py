"""
Subtree of Another Tree

Check if one tree is subtree of another tree.
"""

def is_subtree(root, subroot):
    if not subroot:
        return True
    if not root:
        return False
    
    if is_same_tree(root, subroot):
        return True
    
    return is_subtree(root.left, subroot) or is_subtree(root.right, subroot)

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

if __name__ == "__main__":
    print("Testing Subtree of Another Tree")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")