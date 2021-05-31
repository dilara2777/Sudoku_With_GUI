from random import sample

from Scripts.di_create_sudoku import print_board

base = 3
side = base * base


def sudoku():
    # pattern for a baseline valid solution
    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side

    # randomize rows, columns and numbers (of valid base pattern)
    def shuffle(s):
        return sample(s, len(s))

    r_base = range(base)
    rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, base * base + 1))

    # produce board using randomized baseline pattern
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    return board


def hide_value(board):
    squares = side * side
    empties = squares * 1 // 2
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board


def get_board():
    board = sudoku()
    print_board(board)
    print('\n\n\n')
    hidden_board = hide_value(board)
    print_board(hidden_board)
    return hidden_board

if __name__ == '__main__':
    get_board()
