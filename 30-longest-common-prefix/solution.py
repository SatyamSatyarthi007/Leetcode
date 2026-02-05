"""
Longest Common Prefix

Find longest common prefix among strings.
"""

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

if __name__ == "__main__":
    print("Testing Longest Common Prefix")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")