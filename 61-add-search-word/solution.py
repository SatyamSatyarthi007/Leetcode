"""
Add and Search Word

Design data structure for adding and searching words with wildcard support.
"""

class WordDictionary:
    def __init__(self):
        self.root = {}
    
    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True  # End marker
    
    def search(self, word):
        return self._search_in_node(word, self.root)
    
    def _search_in_node(self, word, node):
        for i, char in enumerate(word):
            if char == '.':
                # Wildcard character - check all possible paths
                for child in node:
                    if child != '#' and self._search_in_node(word[i+1:], node[child]):
                        return True
                return False
            elif char not in node:
                return False
            else:
                node = node[char]
        
        return '#' in node

if __name__ == "__main__":
    print("Testing Add and Search Word")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")