#!/usr/bin/env python3
"""
Script to generate solutions for the missing problems.
"""

import os

# Solutions for missing problems
missing_solutions = {
    "23-smallest-window-containing-substring": {
        "title": "Smallest Window Containing Substring",
        "description": "Find smallest window in string containing all characters of another string.",
        "solution": """def min_window(s, t):
    from collections import Counter
    
    if not s or not t:
        return ""
    
    t_count = Counter(t)
    required = len(t_count)
    formed = 0
    
    window_count = {}
    left = 0
    min_length = float('inf')
    min_left = 0
    
    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        while formed == required and left <= right:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left = left
            
            left_char = s[left]
            window_count[left_char] -= 1
            if left_char in t_count and window_count[left_char] < t_count[left_char]:
                formed -= 1
            left += 1
    
    return "" if min_length == float('inf') else s[min_left:min_left + min_length]"""
    },
    
    "25-group-anagrams": {
        "title": "Group Anagrams",
        "description": "Group strings that are anagrams of each other.",
        "solution": """def group_anagrams(strs):
    from collections import defaultdict
    
    anagram_groups = defaultdict(list)
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagram_groups[sorted_str].append(s)
    
    return list(anagram_groups.values())"""
    },
    
    "29-count-palindromic-substrings": {
        "title": "Count Palindromic Substrings",
        "description": "Count all palindromic substrings in a string.",
        "solution": """def count_substrings(s):
    if not s:
        return 0
    
    def count_palindromes_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    total_count = 0
    
    for i in range(len(s)):
        # Odd length palindromes
        total_count += count_palindromes_around_center(i, i)
        # Even length palindromes
        total_count += count_palindromes_around_center(i, i + 1)
    
    return total_count"""
    },
    
    "31-valid-parentheses": {
        "title": "Valid Parentheses",
        "description": "Check if parentheses are valid and properly nested.",
        "solution": """def is_valid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0"""
    },
    
    "33-detect-cycle": {
        "title": "Detect Cycle in Linked List",
        "description": "Detect if a linked list has a cycle.",
        "solution": """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False"""
    },
    
    "36-remove-nth-node": {
        "title": "Remove Nth Node From End",
        "description": "Remove nth node from end of linked list.",
        "solution": """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    
    # Move fast pointer n steps ahead
    for _ in range(n + 1):
        fast = fast.next
    
    # Move both pointers until fast reaches end
    while fast:
        fast = fast.next
        slow = slow.next
    
    # Remove the nth node
    slow.next = slow.next.next
    
    return dummy.next"""
    },
    
    "38-add-one-linked-list": {
        "title": "Add One to Linked List",
        "description": "Add 1 to a number represented as linked list.",
        "solution": """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_one(head):
    def reverse_list(node):
        prev = None
        current = node
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev
    
    # Reverse the list
    reversed_head = reverse_list(head)
    
    # Add one
    current = reversed_head
    carry = 1
    
    while current and carry:
        total = current.val + carry
        current.val = total % 10
        carry = total // 10
        
        if carry and not current.next:
            current.next = ListNode(0)
        
        current = current.next
    
    # Reverse back
    return reverse_list(reversed_head)"""
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
    """Generate solutions for missing problems."""
    print("Generating solutions for missing problems...")
    
    success_count = 0
    total_count = len(missing_solutions)
    
    for folder_name, problem_data in missing_solutions.items():
        if create_solution_file(folder_name, problem_data):
            if create_readme_file(folder_name, problem_data):
                success_count += 1
    
    print(f"\\nGeneration complete! Successfully created {success_count}/{total_count} missing problems.")

if __name__ == "__main__":
    main()