"""
Set Matrix Zeroes

Set entire row and column to zero if an element is zero.
"""

def set_zeroes(matrix):
    if not matrix or not matrix[0]:
        return
    
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = first_col_zero = False
    
    # Check if first row/column should be zero
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break
    
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    # Use first row/column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    
    # Set zeroes based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Handle first row/column
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

if __name__ == "__main__":
    print("Testing Set Matrix Zeroes")
    print("=" * 50)
    
    # Add test cases specific to this problem
    # This is a template - customize as needed
    print("Add specific test cases for this problem")