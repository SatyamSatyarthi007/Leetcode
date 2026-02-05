"""
Snake and Ladder Problem

Find minimum moves to reach end of snake and ladder board.
"""

from collections import deque

def snakes_and_ladders(board):
    n = len(board)
    
    def get_position(pos):
        row = (pos - 1) // n
        col = (pos - 1) % n
        if row % 2 == 1:  # Odd row - right to left
            col = n - 1 - col
        return n - 1 - row, col
    
    queue = deque([(1, 0)])  # (position, moves)
    visited = {1}
    
    while queue:
        pos, moves = queue.popleft()
        
        if pos == n * n:
            return moves
        
        for i in range(1, 7):
            new_pos = pos + i
            if new_pos > n * n:
                break
            
            row, col = get_position(new_pos)
            if board[row][col] != -1:
                new_pos = board[row][col]
            
            if new_pos not in visited:
                visited.add(new_pos)
                queue.append((new_pos, moves + 1))
    
    return -1

if __name__ == "__main__":
    print("Testing Snake and Ladder Problem")
    print("=" * 50)
    
    # Add test cases specific to this problem
    print("Add specific test cases for this problem")