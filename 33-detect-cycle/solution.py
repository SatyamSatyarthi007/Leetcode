"""
Detect Cycle in Linked List

Detect if a linked list has a cycle.
"""

class ListNode:
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
    
    return False

if __name__ == "__main__":
    print("Testing Detect Cycle in Linked List")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")