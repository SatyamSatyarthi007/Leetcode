"""
Find Middle of Linked List

Find middle element of linked list.
"""

def middle_node(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

if __name__ == "__main__":
    print("Testing Find Middle of Linked List")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")