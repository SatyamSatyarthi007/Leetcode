"""
Top K Frequent Elements

Find k most frequent elements in array.
"""

import heapq
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, _ in count.most_common(k)]

if __name__ == "__main__":
    print("Testing Top K Frequent Elements")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")