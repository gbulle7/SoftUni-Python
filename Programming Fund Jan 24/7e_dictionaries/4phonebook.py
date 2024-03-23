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


# def fill_phonebook():
#     phonebook = {}
#
#     while True:
#         entry = input().split('-')
#
#         if len(entry) == 1:
#             return phonebook, int(entry[0])
#
#         name, number = entry
#         phonebook[name] = number
#
#
# def search_contact(phonebook, name):
#     if name in phonebook:
#         print(f'{name} -> {phonebook[name]}')
#     else:
#         print(f'Contact {name} does not exist.')
#
#
# def main():
#     phonebook, number = fill_phonebook()
#
#     for _ in range(number):
#         search_name = input()
#         search_contact(phonebook, search_name)
#
#
# if __name__ == '__main__':
#     main()
