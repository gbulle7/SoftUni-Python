# method 1
book = input()
book_counter = 0

while True:
    current_book = input()
    if current_book == book:
        print(f'You checked {book_counter} books and found it.')
        break
    elif current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break
    book_counter += 1

# # method 2
# book = input()
# book_counter = 0
# current_book = input()
#
# while current_book != book:
#     if current_book == 'No More Books':
#         print('The book you search is not here!')
#         print(f'You checked {book_counter} books.')
#         break
#     current_book = input()
#     book_counter += 1
# else:
#     print(f'You checked {book_counter} books and found it.')

# method 3
# book = input()
# book_counter = 0
# current_book = input()
#
# while current_book != 'No More Books':
#     if current_book == book:
#         print(f'You checked {book_counter} books and found it.')
#         break
#     current_book = input()
#     book_counter += 1
# else:
#     print('The book you search is not here!')
#     print(f'You checked {book_counter} books.')

# method 4
# book = input()
# book_counter = 0
# is_found = False
# current_book = input()
#
# while current_book != 'No More Books':
#     if current_book == book:
#         is_found = True
#         print(f'You checked {book_counter} books and found it.')
#         break
#     current_book = input()
#     book_counter += 1
# if not is_found:
#     print('The book you search is not here!')
#     print(f'You checked {book_counter} books.')

# method 5
# book_name = input()
# current_book = input()
# book_counter = 0
# book_is_found = False
#
# while current_book != 'No More Books':
#     if current_book == book_name:
#         book_is_found = True
#         break
#     book_counter += 1
#     current_book = input()
# if book_is_found:
#     print(f'You checked {book_counter} books and found it.')
# else:
#     print('The book you search is not here!')
#     print(f'You checked {book_counter} books.')