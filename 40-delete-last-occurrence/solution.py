"""
Delete Last Occurrence

Delete last occurrence of an item from linked list.
"""

def delete_last_occurrence(head, key):
    dummy = ListNode(0)
    dummy.next = head
    
    last_occurrence = None
    current = dummy
    
    while current.next:
        if current.next.val == key:
            last_occurrence = current
        current = current.next
    
    if last_occurrence:
        last_occurrence.next = last_occurrence.next.next
    
    return dummy.next

if __name__ == "__main__":
    print("Testing Delete Last Occurrence")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")