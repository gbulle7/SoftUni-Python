import tkinter as tk
from tkinter import messagebox
from functools import partial

BOARD_SIZE = 3

app_config: dict = {'board': [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)],
                    'buttons': [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)],
                    'sign': 'X',
                    'X': None,
                    'O': None
}


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


def get_content(row, col, window):
    if app_config['board'][row][col] is None:
        app_config['board'][row][col] = app_config['sign']
        app_config['buttons'][row][col].config(text=app_config['board'][row][col])
        if is_win(app_config['board'], app_config['sign']):
            window.destroy()
            messagebox.showinfo('Winner', f"Player {app_config[app_config['sign']]} wins!")
        elif is_draw(app_config['board']):
            window.destroy()
            messagebox.showinfo('Draw', 'The game ended in a draw!')
        app_config['sign'] = 'X' if app_config['sign'] == 'O' else 'O'


def render_board(window):
    grid_frame = tk.Frame(master=window)
    grid_frame.pack(padx=10, pady=10)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            gc = partial(get_content, row, col, window)
            app_config['buttons'][row][col] = tk.Button(
                master=grid_frame,
                command=gc,
                text=app_config['board'][row][col] if app_config['board'][row][col] else ' ',
                width=10,
                height=4
            )
            app_config['buttons'][row][col].grid(row=row, column=col)


def start_game(window, player_one, player_two, player_one_sign, player_two_sign):
    window.destroy()
    window = tk.Tk()
    window.geometry('480x480')
    window.title('Tic Tac Toe')

    app_config['sign'] = player_one_sign
    app_config[player_one_sign] = player_one
    app_config[player_two_sign] = player_two

    p1 = tk.Label(window, text=f'{player_one} plays with {player_one_sign}', width=20)
    p2 = tk.Label(window, text=f'{player_two} plays with {player_two_sign}', width=20)
    p1.pack()
    p2.pack()

    render_board(window)


def start_screen():
    window = tk.Tk()
    window.geometry('480x480')
    window.title('Tic Tac Toe')

    tk.Label(window, text='First player name: ').pack()
    player_one = tk.Entry(window)
    player_one.pack()
    p_one_sign = tk.StringVar()
    p_one_sign.set('X')
    tk.Label(window, text='Choose sign for first player:').pack()
    tk.Radiobutton(window, text='X', variable=p_one_sign, value='X').pack()
    tk.Radiobutton(window, text='O', variable=p_one_sign, value='O').pack()
    tk.Label(window, text='Second player name: ').pack()
    player_two = tk.Entry(window)
    player_two.pack()
    tk.Button(window, text='Start Game',
              command=lambda: start_game(window,
                                         player_one.get(),
                                         player_two.get(),
                                         p_one_sign.get(),
                                         'X' if p_one_sign.get() == 'O' else 'O')).pack()

    window.mainloop()


if __name__ == '__main__':
    start_screen()
