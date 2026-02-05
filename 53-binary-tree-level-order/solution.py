"""
Binary Tree Level Order Traversal

Perform level order traversal of binary tree.
"""

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

if __name__ == "__main__":
    print("Testing Binary Tree Level Order Traversal")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")