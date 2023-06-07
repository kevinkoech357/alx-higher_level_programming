#!/usr/bin/python3

"""
This program solves the N-queens problem which is a challenge of
placing N non-attacking queens on an NxN chessboard.
"""


def check_safety(board, row, column):
    """
    Checks if a position is safe from attack by other queens.

    Args:
        board (list): The board state represented by list.
        row (int): The row index of position to be checked.
        column (int): The column index of position to be checked.

    Return:
        True if position is safe.
        False if otherwise.
    """
    for j in range(column):
        if board[j] == row or abs(board[j] - row) == abs(j - column):
            return False
    return True


def check_board(board, column):
    """
    Check the board state column by column recursively using backtracking.

    Args:
        board (list): The current board state represented by a list.
        column (int): The current column index to check.
    """
    n = len(board)
    if column == n:
        print(str([[j, board[j]] for j in range(n)]))
        return

    for row in range(n):
        if check_safety(board, row, column):
            board[column] = row
            check_board(board, column + 1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = 0
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0 for column in range(n)]
    check_board(board, 0)
