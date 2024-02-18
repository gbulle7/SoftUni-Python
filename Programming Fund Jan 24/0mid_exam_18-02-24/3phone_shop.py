phones = input().split(', ')
command = input().split(' - ')

while command[0] != 'End':
    event = command[0]
    phone = command[1]

    if event == 'Add':
        if phone not in phones:
            phones.append(phone)
    elif event == 'Remove':
        if phone in phones:
            phones.remove(phone)
    elif event == 'Bonus phone':
        old_phone, new_phone = phone.split(':')
        if old_phone in phones:
            phones.insert(phones.index(old_phone) + 1, new_phone)
    elif event == 'Last':
        if phone in phones:
            phones.remove(phone)
            phones.append(phone)

    command = input().split(' - ')

print(', '.join(phones))