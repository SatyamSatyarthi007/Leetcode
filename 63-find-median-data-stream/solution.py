"""
Find Median from Data Stream

Find median of data stream using two heaps.
"""

import heapq

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
        return (-self.small[0] + self.large[0]) / 2

if __name__ == "__main__":
    print("Testing Find Median from Data Stream")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")