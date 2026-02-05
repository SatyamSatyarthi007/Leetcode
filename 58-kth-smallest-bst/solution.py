"""
Kth Smallest Element in BST

Find kth smallest element in binary search tree.
"""

def kth_smallest(root, k):
    def inorder(node):
        if not node:
            return
        
        inorder(node.left)
        
        nonlocal count, result
        count += 1
        if count == k:
            result = node.val
            return
        
        inorder(node.right)
    
    count = 0
    result = None
    inorder(root)
    return result

if __name__ == "__main__":
    print("Testing Kth Smallest Element in BST")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")