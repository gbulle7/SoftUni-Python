def is_sign_valid(sign):
    return sign in ['X', 'O']


def is_choice_valid(choice_, board_mapper_, board_):
    if not choice_.isdigit():
        return False
    choice_ = int(choice_)
    if choice_ not in board_mapper:
        return False
    if board_[board_mapper_[choice_][0]][board_mapper_[choice_][1]]:
        return False
    return True


def render_board(board_):
    for row in board_:
        print(f"|  {'  |  '.join(sign if sign else ' ' for sign in row)}  |")


def is_win_rows(board_):
    for row in board_:
        if len(set(row)) == 1 and row[0] is not None:      # Can do with if row.count(choice_) == len(row)
            return True
    return False


def is_win_cols(board_, curr_sign):
    for col_ in range(len(board_)):
        current_col = []
        for row_ in range(len(board_)):
            current_col.append(board_[row_][col_] == curr_sign)
        if all(current_col):
            return True
    return False


def is_win_diagonals(board_, curr_sign):
    diagonal_1, diagonal_2 = [], []
    for idx in range(len(board_)):
        diagonal_1.append(board_[idx][idx] == curr_sign)
        diagonal_2.append(board_[idx][len(board_) - 1 - idx] == curr_sign)
    return all(diagonal_1) or all(diagonal_2)


def is_win(board_, curr_sign):
    return any([is_win_rows(board_), is_win_cols(board_, curr_sign), is_win_diagonals(board_, curr_sign)])


def is_win_row_possible(board_):
    return not all(['X' in row_ and 'O' in row_ for row_ in board_])


def is_win_col_possible(board_):
    columns = []
    for col_ in range(len(board_)):
        current_col = [board_[row_][col_] for row_ in range(len(board_))]
        columns.append('X' in current_col and 'O' in current_col)
    return not all(columns)


def is_win_diagonal_possible(board_):
    diagonal_1, diagonal_2 = [], []
    for idx in range(len(board_)):
        diagonal_1.append(board_[idx][idx])
        diagonal_2.append(board_[idx][len(board_) - 1 - idx])
    if 'X' in diagonal_1 and 'O' in diagonal_1 and 'X' in diagonal_2 and 'O' in diagonal_1:
        return False
    return True


def is_draw(board_):
    return not any([is_win_row_possible(board_), is_win_col_possible(board_), is_win_diagonal_possible(board_)])


BOARD_SIZE = 3
player_one = input('Player one name: ').strip()
player_two = input('Player two name: ').strip()


while True:
    player_one_sign = input(f"{player_one}, would you like to play with 'X' or 'O'? ").upper()
    if is_sign_valid(player_one_sign):
        break
player_two_sign = 'X' if player_one_sign == 'O' else 'O'

board: list = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
board_mapper = {i + 1: (i // BOARD_SIZE, i % BOARD_SIZE) for i in range(BOARD_SIZE ** 2)}

print('This is the numeration of the board:')
[print(f"|  {'  |  '.join([str(i + 1 + row * BOARD_SIZE) for i in range(BOARD_SIZE)])}  |") for row in range(BOARD_SIZE)]
print(f'{player_one} starts first!')

turn = 1
while True:
    current_player, current_sign = (player_one, player_one_sign) if turn % 2 else (player_two, player_two_sign)
    while True:
        choice = input(f'{current_player}, choose a free position [1-9]: ').strip()
        if is_choice_valid(choice, board_mapper, board):
            break

    row, col = board_mapper[int(choice)]
    board[row][col] = current_sign
    render_board(board)

    if is_win(board, current_sign):
        print(f'{current_player} won!')
        break

    if is_draw(board):
        print(f'Draw!')
        break

    turn += 1
