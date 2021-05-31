import random

BOX_SIZE = 3


def create_filled_board():
    # generate empty board
    row = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(board)):
        board[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # fill out the board I need 3 condition met
    for i in range(len(board)):
        for j in range(len(board[0])):
            n = get_unique_value(board, i, j)
            board[i][j] = n
    return board

def is_fit_row(board, i, n):
    # is in this row not present?
    row = board[i]
    if n in row:
        return False
    return True

def is_fit_col(board, j, n):
    # is in this col not present?
    col = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for k in range(9):
        col[k] = board[k][j]
    if n in col:
        return False
    return True

def is_fit_box(board,x,y, n):
    #is in this box not present?
    box = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    row_x = x // BOX_SIZE
    row_y = y // BOX_SIZE
    for k in range(BOX_SIZE):
        for f in range(BOX_SIZE):
            box[k * BOX_SIZE + f] = board[row_x * BOX_SIZE + k][row_y * BOX_SIZE + f]
    if n in box:
        return False
    return True

def get_unique_value(board, x, y):
    possible_n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # for k in range(9):
    while possible_n:
        random_index = random.randint(0, len(possible_n) - 1)
        n = possible_n[random_index]
        print(n)
        row = is_fit_row(board, x, n)
        col = is_fit_col(board, y, n)
        box = is_fit_box(board,x, y, n)

        if row and col and box:
            print("------------------------",(row and col and box),n, possible_n, row, col, box, ", n = ", n, " i/j = ", x, y)
            break
        # print(n)
        possible_n.remove(n)

    print( (row and col and box), n, possible_n, row, col, box, ", n = ", n, " i/j = ", x, y)
    return n


def hide_value(board, DIFFICULTIES):
    koefiicient_hiden_values = 0
    how_many_values = BOX_SIZE ** 4  # total 81 value, 9* box(3*3)
    if DIFFICULTIES == 1:
        koefiicient_hiden_values = 0.46  # 37 hide
    if DIFFICULTIES == 2:
        koefiicient_hiden_values = 0.55  # 37 left, 44 hide
    if DIFFICULTIES == 3:
        koefiicient_hiden_values = 0.62  # 50 hide
    how_many_values_to_hide = int(how_many_values * koefiicient_hiden_values)

    for i in range(how_many_values_to_hide):
        x = random.randint(0, 8)
        y = random.randint(0, 8)

        while board[x][y] == 0:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
        board[x][y] = 0

    print_board(board)
    return board


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('-----------------------')

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')


def create_board_with_hiden_values():
    board = create_filled_board()
    print("printing board from  ")
    print_board(board)
    print('\n\n------------------------------------------\n\n')
    # difficulties = input("Please enter difficulty level, 1 - easy, 2 - middle, 3 - hard, 0 - exit")
    # while difficulties not in ["1","2","3", "0"]:
    #     difficulties = input("Please enter difficulty level, 1 - easy, 2 - middle, 3 - hard, only 1 or 2 or 3 or 0 for exit")
    # if difficulties == "0":
    #     return
    # print(board)
    # hidden_board = hide_value(board, int(difficulties))
    hidden_board = hide_value(board, 2)
    print(hidden_board)
    return board


def main():
    board = create_board_with_hiden_values()
    print_board(board)


if __name__ == '__main__':
    main()
