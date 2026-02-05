"""
Reorder List

Reorder linked list in alternating first and last order.
"""

def reorder_list(head):
    if not head or not head.next:
        return
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev = None
    current = slow
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    # Merge two halves
    first = head
    second = prev
    
    while second.next:
        temp1 = first.next
        temp2 = second.next
        
        first.next = second
        second.next = temp1
        
        first = temp1
        second = temp2

if __name__ == "__main__":
    print("Testing Reorder List")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")