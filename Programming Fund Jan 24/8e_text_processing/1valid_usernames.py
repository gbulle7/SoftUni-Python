usernames = input().split(', ')

for name in usernames:
    if 3 <= len(name) <= 16:
        if name.isalnum() or ([char.isalnum() for char in name] and ('-' in name or '_' in name)):
            print(name)


# def length_is_valid(name):
#     if 3 <= len(name) <= 16:
#         return True
#     return False
#
#
# def characters_are_valid(name):
#     for character in name:
#         if not (character.isalnum() or character == "-" or character == "_"):
#             return False
#     return True
#
#
# def no_redundant_symbols(name):
#     if " " in name:
#         return False
#     return True
#
#
# def username_is_valid(name):
#     if length_is_valid(name) and characters_are_valid(name) and no_redundant_symbols(name):
#         return True
#     return False
#
#
# usernames = input().split(", ")
# for username in usernames:
#     if username_is_valid(username):
#         print(username)


# def valid_username(username):
#     allowed_symbols = ['_', '-']
#     if 3 <= len(username) <= 16:
#         for character in username:
#             if character.isalnum() or character in allowed_symbols:
#                 continue
#             return
#     else:
#         return
#     print(username)
#
#
# list_usernames = input().split(', ')
# while len(list_usernames):
#     name = list_usernames[0]
#     valid_username(name)
#     list_usernames.pop(0)
