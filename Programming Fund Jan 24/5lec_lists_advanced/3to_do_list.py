notes = ['0'] * 10

while True:
    command = input()
    if command == 'End':
        break

    units = command.split('-')
    order = int(units[0]) - 1
    note = units[1]
    notes.pop(order)
    notes.insert(order, note)

notes = [note for note in notes if note != '0']
print(notes)


# Judge 1 error; 80/100
# notes = []
# final_notes = []
#
# while True:
#     command = input()
#
#     if command == 'End':
#         break
#
#     notes.append(command)
#
# notes.sort()
# for note in notes:
#     final_notes.append(note.split('-')[1])
#
# print(final_notes)
