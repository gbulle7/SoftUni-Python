phonebook = {}

while True:
    name_phone = input()
    if name_phone.isdigit():
        break
    name, phone = name_phone.split('-')
    phonebook[name] = phone

for num in range(int(name_phone)):
    contact_name = input()
    if contact_name not in phonebook:
        print(f'Contact {contact_name} does not exist.')
    else:
        print(f'{contact_name} -> {phonebook[contact_name]}')
