"""
Check Same Tree Structure

Check if two binary trees have same structure.
"""

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))

if __name__ == "__main__":
    print("Testing Check Same Tree Structure")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")