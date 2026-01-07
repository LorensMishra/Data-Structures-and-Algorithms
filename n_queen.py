def print_board(board, n):
    """
    Print the chessboard with queens positions.
    'Q' represents a queen, '.' represents empty cell.
    """
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")  # Queen placed
            else:
                print(".", end=" ")  # Empty cell
        print()  # new line for next row
    print("-" * (2 * n))  # separator after board


def is_safe(board, row, col, n):
    """
    Check if placing a queen at (row, col) is safe.
    Must check:
        1. Same column above
        2. Left diagonal above
        3. Right diagonal above
    """
    # 1. Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # 2. Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # 3. Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True  # Safe to place queen


def solve_n_queens(board, row, n, solutions):
    """
    Recursive function to solve N-Queens problem using backtracking.
    board     : current chessboard
    row       : current row to place a queen
    n         : size of board (N x N)
    solutions : list to store total solutions
    """
    if row == n:  # Base case: all queens are placed
        print_board(board, n)  # print current solution
        solutions.append(1)    # count this solution
        return

    # Try placing queen in all columns of current row
    for col in range(n):
        if is_safe(board, row, col, n):  # if safe
            board[row][col] = 1          # place queen
            solve_n_queens(board, row + 1, n, solutions)  # recurse for next row
            board[row][col] = 0          # backtrack (remove queen)


def main():
    n = int(input("Enter number of queens (N): "))  # Runtime input
    board = [[0 for _ in range(n)] for _ in range(n)]  # Initialize empty board
    solutions = []  # List to store/count solutions

    solve_n_queens(board, 0, n, solutions)  # Start solving from row 0

    print(f"\nTotal solutions for N = {n}: {len(solutions)}")  # Print total solutions


if __name__ == "__main__":
    main()  # Run the program
