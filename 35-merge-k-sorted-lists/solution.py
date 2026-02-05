"""
Merge K Sorted Lists

Merge k sorted linked lists.
"""

import heapq

def merge_k_lists(lists):
    if not lists:
        return None
    
    heap = []
    
    # Add first node of each list to heap
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

if __name__ == "__main__":
    print("Testing Merge K Sorted Lists")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")