"""
Binary Tree Maximum Path Sum

Find maximum path sum in binary tree.
"""

def max_path_sum(root):
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        
        # Get maximum gain from left and right subtrees
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Current path sum
        current_path_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_path_sum)
        
        return node.val + max(left_gain, right_gain)
    
    max_sum = float('-inf')
    max_gain(root)
    return max_sum

if __name__ == "__main__":
    print("Testing Binary Tree Maximum Path Sum")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")