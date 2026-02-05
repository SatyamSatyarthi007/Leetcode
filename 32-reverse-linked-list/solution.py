"""
Reverse Linked List

Reverse a singly linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

if __name__ == "__main__":
    print("Testing Reverse Linked List")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")