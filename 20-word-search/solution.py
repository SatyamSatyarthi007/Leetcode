"""
Word Search

Find if a word exists in a 2D grid of characters.
"""

def exist(board, word):
    if not board or not board[0] or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def dfs(i, j, k):
        if k == len(word):
            return True
        if (i < 0 or i >= rows or j < 0 or j >= cols or 
            board[i][j] != word[k]):
            return False
        
        temp = board[i][j]
        board[i][j] = '#'
        
        found = (dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or 
                dfs(i, j+1, k+1) or dfs(i, j-1, k+1))
        
        board[i][j] = temp
        return found
    
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    
    return False

if __name__ == "__main__":
    print("Testing Word Search")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")