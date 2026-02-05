"""
Add One to Linked List

Add 1 to a number represented as linked list.
"""

class ListNode:
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
    return reverse_list(reversed_head)

if __name__ == "__main__":
    print("Testing Add One to Linked List")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")