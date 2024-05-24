size = 5
targets_shot = []
remaining_targets = 0
matrix = []
a_row, a_col = (0, 0)

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'A':
            a_row, a_col = row, col
        elif matrix[row][col] == 'x':
            remaining_targets += 1


def shoot(direction, mat, r, c):
    t_shot = False
    t_psn = (0, 0)
    while (r in range(len(mat)) and c in range(len(mat))) and not t_shot:
        if direction == 'up' and (r - 1) in range(len(mat)):
            if mat[r - 1][c] == 'x':
                t_shot = True
                t_psn = (r - 1, c)
                break
            r -= 1
            continue
        elif direction == 'down' and (r + 1) in range(len(mat)):
            if mat[r + 1][c] == 'x':
                t_shot = True
                t_psn = (r + 1, c)
                break
            r += 1
            continue
        elif direction == 'left' and (c - 1) in range(len(mat)):
            if mat[r][c - 1] == 'x':
                t_shot = True
                t_psn = (r, c - 1)
                break
            c -= 1
            continue
        elif direction == 'right' and (c + 1) in range(len(mat)):
            if mat[r][c + 1] == 'x':
                t_shot = True
                t_psn = (r, c + 1)
                break
            c += 1
            continue
        break
    t_row, t_col = t_psn
    return t_shot, t_row, t_col


def move(direction, steps, mat, r, c):
    a_r, a_c = r, c
    if direction == 'up':
        a_r, a_c = r - steps, c
    elif direction == 'down':
        a_r, a_c = r + steps, c
    elif direction == 'left':
        a_r, a_c = r, c - steps
    elif direction == 'right':
        a_r, a_c = r, c + steps
    if a_r in range(len(mat)) and a_c in range(len(mat)) and mat[a_r][a_c] == '.':
        mat[r][c] = '.'
        mat[a_r][a_c] = 'A'
        r, c = a_r, a_c
    return r, c


cmds = int(input())
for _ in range(cmds):
    command = input().split()
    if command[0] == 'move':
        a_row, a_col = move(command[1], int(command[2]), matrix, a_row, a_col)
    elif command[0] == 'shoot':
        target_shot, target_r, target_c = shoot(command[1], matrix, a_row, a_col)
        if target_shot:
            matrix[target_r][target_c] = '.'
            targets_shot.append([target_r, target_c])
            remaining_targets -= 1
    if not remaining_targets:
        break

if remaining_targets:
    print(f"Training not completed! {remaining_targets} targets left.")
else:
    print(f'Training completed! All {len(targets_shot)} targets hit.')
[print(target) for target in targets_shot]


# Method 2
# def move(direction, steps, r, c):
#     if direction == 'up':
#         a_r, a_c = r - steps, c
#     elif direction == 'down':
#         a_r, a_c = r + steps, c
#     elif direction == 'left':
#         a_r, a_c = r, c - steps
#     elif direction == 'right':
#         a_r, a_c = r, c + steps
#     if a_r in range(size) and a_c in range(size) and matrix[a_r][a_c] == '.':
#         matrix[r][c] = '.'
#         r, c = a_r, a_c
#         matrix[r][c] = 'A'
#     return r, c
#
#
# def shoot(direction, r, c):
#     possible_targets = []
#     if direction == "up":
#         possible_targets.extend([[row, c] for row in range(r - 1, - 1, - 1)])
#     elif direction == "down":
#         possible_targets.extend([[row, c] for row in range(r + 1, size)])
#     elif direction == "left":
#         possible_targets.extend([[r, col] for col in range(c - 1, - 1, - 1)])
#     elif direction == "right":
#         possible_targets.extend([[r, col] for col in range(c + 1, size)])
#     for target in possible_targets:
#         t_row, t_col = target
#         if t_row in range(size) and t_col in range(size) and matrix[t_row][t_col] == "x":
#             matrix[t_row][t_col] = "."
#             return [t_row, t_col]
#     return []
#
#
# size = 5
# targets_shot = []
# remaining_targets = 0
# matrix = []
# a_row, a_col = 0, 0
#
# for m_row in range(size):
#     curr_row = [x for x in input().split()]
#     matrix.append(curr_row)
#     for symbol in curr_row:
#         if symbol == 'A':
#             a_row, a_col = m_row, curr_row.index('A')
#         elif symbol == "x":
#             remaining_targets += 1
#
# cmds = int(input())
#
# for _ in range(cmds):
#     command = input().split()
#     if command[0] == 'move':
#         move_dir, step = command[1], int(command[2])
#         a_row, a_col = move(move_dir, step, a_row, a_col)
#     elif command[0] == 'shoot':
#         shoot_dir = command[1]
#         t_psn = shoot(shoot_dir, a_row, a_col)
#         if t_psn:
#             targets_shot.append(t_psn)
#             remaining_targets -= 1
#     if remaining_targets == 0:
#         break
#
# if remaining_targets == 0:
#     print(f"Training completed! All {len(targets_shot)} targets hit.")
# else:
#     print(f"Training not completed! {remaining_targets} targets left.")
#
# [print(target) for target in targets_shot]