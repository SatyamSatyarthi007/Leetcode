"""
Flood Fill Algorithm

Implement flood fill to replace connected region with new color.
"""

def flood_fill(image, sr, sc, new_color):
    if not image or image[sr][sc] == new_color:
        return image
    
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]
    
    def dfs(i, j):
        if (i < 0 or i >= rows or j < 0 or j >= cols or 
            image[i][j] != original_color):
            return
        
        image[i][j] = new_color
        
        # Explore 4 directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    
    dfs(sr, sc)
    return image

if __name__ == "__main__":
    print("Testing Flood Fill Algorithm")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")