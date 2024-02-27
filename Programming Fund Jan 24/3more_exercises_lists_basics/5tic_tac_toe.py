first_row = input().split()
second_row = input().split()
third_row = input().split()

player = 1
name_player = "First"
winner_found = False

while player <= 2:  # check winner
    player = str(player)
    line = [player, player, player]
    if first_row == line or second_row == line or third_row == line:    # rows
        winner_found = True
        break
    for column in range(3):
        if first_row[column] == player and second_row[column] == player and third_row[column] == player:    # columns
            winner_found = True
            break
    if first_row[0] == player and second_row[1] == player and third_row[2] == player:   # first diagonal
        winner_found = True
        break
    elif first_row[2] == player and second_row[1] == player and third_row[0] == player:  # second diagonal
        winner_found = True
        break
    player = int(player) + 1
    name_player = "Second"

if winner_found:
    print(f"{name_player} player won")
else:
    print("Draw!")



# def check_win(board, player):
#     # check row
#     for row in board:
#         if row.count(player) == 3:
#             return True
#
#     # check column
#     for col_index in range(3):
#         column = [row[col_index] for row in board]
#         if column.count(player) == 3:
#             return True
#
#     # check diagonals
#     first_diagonal = [board[element][element] for element in range(3)]
#     if first_diagonal.count(player) == 3:
#         return True
#
#     second_diagonal = [board[element][2 - element] for element in range(3)]
#     if second_diagonal.count('1') == 3:
#         return True
#
#
# board = []
# for winner in range(3):
#     board.append(input().split())
#
# if check_win(board, '1'):
#     print("First player won")
# elif check_win(board, '2'):
#     print("Second player won")
# else:
#     print("Draw!")