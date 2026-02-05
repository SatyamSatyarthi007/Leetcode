"""
Group Anagrams

Group strings that are anagrams of each other.
"""

def group_anagrams(strs):
    from collections import defaultdict
    
    anagram_groups = defaultdict(list)
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagram_groups[sorted_str].append(s)
    
    return list(anagram_groups.values())

if __name__ == "__main__":
    print("Testing Group Anagrams")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")