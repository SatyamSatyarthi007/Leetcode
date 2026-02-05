"""
Largest Region in Boolean Matrix

Find largest region of connected 1s in boolean matrix.
"""

def largest_region(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    max_region = 0
    
    def dfs(i, j):
        if (i < 0 or i >= rows or j < 0 or j >= cols or 
            matrix[i][j] == 0):
            return 0
        
        matrix[i][j] = 0  # Mark as visited
        region_size = 1
        
        # Check all 8 directions
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                     (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for di, dj in directions:
            region_size += dfs(i + di, j + dj)
        
        return region_size
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                max_region = max(max_region, dfs(i, j))
    
    return max_region

if __name__ == "__main__":
    print("Testing Largest Region in Boolean Matrix")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")