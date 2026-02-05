"""
Serialize and Deserialize Binary Tree

Serialize and deserialize binary tree.
"""

def serialize(root):
    def preorder(node):
        if not node:
            result.append("None")
            return
        result.append(str(node.val))
        preorder(node.left)
        preorder(node.right)
    
    result = []
    preorder(root)
    return ','.join(result)

def deserialize(data):
    def build():
        val = next(values)
        if val == "None":
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node
    
    values = iter(data.split(','))
    return build()

if __name__ == "__main__":
    print("Testing Serialize and Deserialize Binary Tree")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")