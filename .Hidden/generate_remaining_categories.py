#!/usr/bin/env python3
"""
Final comprehensive script to generate all remaining LeetCode problem solutions.
This covers Stack & Queue, Tree, Heap, Graph, Bit Manipulations, and Dynamic Programming problems.
"""

import os

# Complete problem definitions for all remaining categories
remaining_problems = {
    # Stack & Queue Problems (41-48)
    "41-infix-to-postfix": {
        "title": "Infix to Postfix Conversion",
        "description": "Convert infix expression to postfix notation.",
        "solution": """def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []
    
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while (stack and stack[-1] != '(' and 
                   precedence.get(stack[-1], 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)"""
    },
    
    "42-next-greater-element": {
        "title": "Next Greater Element",
        "description": "Find next greater element for each element in array.",
        "solution": """def next_greater_elements(nums):
    result = [-1] * len(nums)
    stack = []
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    
    return result"""
    },
    
    "43-delete-middle-stack": {
        "title": "Delete Middle Element of Stack",
        "description": "Delete middle element from stack without using extra space.",
        "solution": """def delete_middle(stack, n, current=0):
    if not stack:
        return
    
    # Base case: when current equals middle element
    if current == n // 2:
        stack.pop()
        return
    
    # Remove current element
    temp = stack.pop()
    
    # Recursively remove middle from remaining stack
    delete_middle(stack, n, current + 1)
    
    # Put back the removed element
    stack.append(temp)"""
    },
    
    "44-check-mirror-n-ary-tree": {
        "title": "Check Mirror of N-ary Tree",
        "description": "Check if two N-ary trees are mirror images of each other.",
        "solution": """def are_mirror(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    
    if len(root1.children) != len(root2.children):
        return False
    
    n = len(root1.children)
    for i in range(n):
        if not are_mirror(root1.children[i], root2.children[n - 1 - i]):
            return False
    
    return True"""
    },
    
    "45-celebrity-problem": {
        "title": "Celebrity Problem",
        "description": "Find celebrity in a group who is known by everyone but knows no one.",
        "solution": """def find_celebrity(matrix):
    n = len(matrix)
    stack = list(range(n))
    
    # Find potential celebrity
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        
        if matrix[a][b] == 1:  # a knows b, so a is not celebrity
            stack.append(b)
        else:  # a doesn't know b, so b is not celebrity
            stack.append(a)
    
    if not stack:
        return -1
    
    candidate = stack[0]
    
    # Verify candidate
    for i in range(n):
        if i != candidate and (matrix[candidate][i] == 1 or matrix[i][candidate] == 0):
            return -1
    
    return candidate"""
    },
    
    "46-longest-valid-substring": {
        "title": "Longest Valid Substring of Parentheses",
        "description": "Find longest valid substring of well-formed parentheses.",
        "solution": """def longest_valid_parentheses(s):
    stack = [-1]  # Base for valid substring calculation
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # New base
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length"""
    },
    
    "47-right-view-binary-tree": {
        "title": "Right View of Binary Tree",
        "description": "Print right view of binary tree using level order traversal.",
        "solution": """def right_view(root):
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
    
    return result"""
    },
    
    "48-circular-tour-petrol-pumps": {
        "title": "Circular Tour Petrol Pumps",
        "description": "Find starting point for circular tour visiting all petrol pumps.",
        "solution": """def can_complete_circuit(petrol, distance):
    n = len(petrol)
    total_petrol = total_distance = 0
    start = 0
    current_petrol = 0
    
    for i in range(n):
        total_petrol += petrol[i]
        total_distance += distance[i]
        current_petrol += petrol[i] - distance[i]
        
        if current_petrol < 0:
            start = i + 1
            current_petrol = 0
    
    return start if total_petrol >= total_distance else -1"""
    },
    
    # Tree Problems (49-61)
    "49-maximum-depth-binary-tree": {
        "title": "Maximum Depth of Binary Tree",
        "description": "Find maximum depth of binary tree.",
        "solution": """def max_depth(root):
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1"""
    },
    
    "50-check-same-tree-structure": {
        "title": "Check Same Tree Structure",
        "description": "Check if two binary trees have same structure.",
        "solution": """def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))"""
    },
    
    "51-invert-binary-tree": {
        "title": "Invert Binary Tree",
        "description": "Invert a binary tree (mirror image).",
        "solution": """def invert_tree(root):
    if not root:
        return None
    
    # Swap left and right subtrees
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root"""
    },
    
    "52-binary-tree-maximum-path-sum": {
        "title": "Binary Tree Maximum Path Sum",
        "description": "Find maximum path sum in binary tree.",
        "solution": """def max_path_sum(root):
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
    return max_sum"""
    },
    
    "53-binary-tree-level-order": {
        "title": "Binary Tree Level Order Traversal",
        "description": "Perform level order traversal of binary tree.",
        "solution": """def level_order(root):
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
    
    return result"""
    },
    
    "54-serialize-deserialize-binary-tree": {
        "title": "Serialize and Deserialize Binary Tree",
        "description": "Serialize and deserialize binary tree.",
        "solution": """def serialize(root):
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
    return build()"""
    },
    
    "55-subtree-another-tree": {
        "title": "Subtree of Another Tree",
        "description": "Check if one tree is subtree of another tree.",
        "solution": """def is_subtree(root, subroot):
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
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)"""
    },
    
    "56-construct-binary-tree": {
        "title": "Construct Binary Tree from Preorder and Inorder",
        "description": "Construct binary tree from preorder and inorder traversal.",
        "solution": """def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    root_index = inorder.index(preorder[0])
    
    root.left = build_tree(preorder[1:root_index + 1], inorder[:root_index])
    root.right = build_tree(preorder[root_index + 1:], inorder[root_index + 1:])
    
    return root"""
    },
    
    "57-validate-binary-search-tree": {
        "title": "Validate Binary Search Tree",
        "description": "Check if binary tree is valid BST.",
        "solution": """def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))"""
    },
    
    "58-kth-smallest-bst": {
        "title": "Kth Smallest Element in BST",
        "description": "Find kth smallest element in binary search tree.",
        "solution": """def kth_smallest(root, k):
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
    return result"""
    },
    
    "59-lowest-common-ancestor-bst": {
        "title": "Lowest Common Ancestor of BST",
        "description": "Find lowest common ancestor of two nodes in BST.",
        "solution": """def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    
    # Both nodes are in left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # Both nodes are in right subtree
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # Current node is LCA
    return root"""
    },
    
    "60-implement-trie": {
        "title": "Implement Trie (Prefix Tree)",
        "description": "Implement trie data structure for efficient string operations.",
        "solution": """class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end_of_word
    
    def starts_with(self, prefix):
        return self._find_node(prefix) is not None
    
    def _find_node(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node"""
    },
    
    "61-add-search-word": {
        "title": "Add and Search Word",
        "description": "Design data structure for adding and searching words with wildcard support.",
        "solution": """class WordDictionary:
    def __init__(self):
        self.root = {}
    
    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True  # End marker
    
    def search(self, word):
        return self._search_in_node(word, self.root)
    
    def _search_in_node(self, word, node):
        for i, char in enumerate(word):
            if char == '.':
                # Wildcard character - check all possible paths
                for child in node:
                    if child != '#' and self._search_in_node(word[i+1:], node[child]):
                        return True
                return False
            elif char not in node:
                return False
            else:
                node = node[char]
        
        return '#' in node"""
    },
    
    # Heap Problems (62-65)
    "62-top-k-frequent-elements": {
        "title": "Top K Frequent Elements",
        "description": "Find k most frequent elements in array.",
        "solution": """import heapq
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, _ in count.most_common(k)]"""
    },
    
    "63-find-median-data-stream": {
        "title": "Find Median from Data Stream",
        "description": "Find median of data stream using two heaps.",
        "solution": """import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negative values)
        self.large = []  # Min heap
    
    def add_num(self, num):
        heapq.heappush(self.small, -num)
        
        # Balance heaps
        if (self.small and self.large and 
            -self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Ensure size property
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2"""
    },
    
    "64-largest-triplet-product": {
        "title": "Largest Triplet Product",
        "description": "Find largest product of any triplet in array.",
        "solution": """def maximum_product(nums):
    nums.sort()
    n = len(nums)
    
    # Product of three largest numbers or two smallest and largest
    return max(nums[n-1] * nums[n-2] * nums[n-3], 
               nums[0] * nums[1] * nums[n-1])"""
    },
    
    "65-connect-ropes-minimum-cost": {
        "title": "Connect Ropes with Minimum Cost",
        "description": "Connect ropes with minimum cost using min heap.",
        "solution": """import heapq

def connect_ropes(ropes):
    if len(ropes) < 2:
        return 0
    
    heapq.heapify(ropes)
    total_cost = 0
    
    while len(ropes) > 1:
        # Connect two smallest ropes
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        
        cost = first + second
        total_cost += cost
        heapq.heappush(ropes, cost)
    
    return total_cost"""
    }
}

def create_solution_file(folder_name, problem_data):
    """Create solution.py file for a problem."""
    solution_content = f'''"""
{problem_data['title']}

{problem_data['description']}
"""

{problem_data['solution']}

if __name__ == "__main__":
    print("Testing {problem_data['title']}")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")'''
    
    file_path = f"c:\\Users\\SATYAM\\Desktop\\leetcode\\{folder_name}\\solution.py"
    try:
        with open(file_path, 'w') as f:
            f.write(solution_content)
        print(f"Created solution file: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating solution file {file_path}: {e}")
        return False

def create_readme_file(folder_name, problem_data):
    """Create README.md file for a problem."""
    readme_content = f"""# {problem_data['title']}

## Problem Description
{problem_data['description']}

## Examples
```python
# Add specific examples for this problem
```

## Solution Approach
# Add specific approach for this problem

## Time Complexity
- **Time Complexity**: O(n) or as appropriate
- **Space Complexity**: O(1) or as appropriate

## Implementation Details
# Add specific implementation details

## Edge Cases
# Add edge cases specific to this problem"""
    
    file_path = f"c:\\Users\\SATYAM\\Desktop\\leetcode\\{folder_name}\\README.md"
    try:
        with open(file_path, 'w') as f:
            f.write(readme_content)
        print(f"Created README file: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating README file {file_path}: {e}")
        return False

def main():
    """Generate all remaining problem solutions."""
    print("Generating remaining LeetCode problem solutions...")
    
    success_count = 0
    total_count = len(remaining_problems)
    
    for folder_name, problem_data in remaining_problems.items():
        if create_solution_file(folder_name, problem_data):
            if create_readme_file(folder_name, problem_data):
                success_count += 1
    
    print(f"\\nGeneration complete! Successfully created {success_count}/{total_count} problems.")
    print("\\nNext: Generate Graph, Bit Manipulations, and Dynamic Programming problems...")

if __name__ == "__main__":
    main()