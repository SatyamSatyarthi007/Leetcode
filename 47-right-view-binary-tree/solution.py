"""
Right View of Binary Tree

Print right view of binary tree using level order traversal.
"""

def right_view(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.pop(0)
            
            # Add rightmost element of each level
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

if __name__ == "__main__":
    print("Testing Right View of Binary Tree")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")