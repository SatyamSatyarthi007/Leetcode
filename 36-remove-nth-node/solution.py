"""
Remove Nth Node From End

Remove nth node from end of linked list.
"""

class ListNode:
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
    
    return dummy.next

if __name__ == "__main__":
    print("Testing Remove Nth Node From End")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")