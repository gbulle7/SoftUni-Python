first_string = input()
second_string = input()

while first_string in second_string:
    second_string = second_string.replace(first_string, '')
print(second_string)

# def replace_substr(string: str, substring: str):
#     if substring not in string:
#         return string
#
#     result = string.replace(substring, '')
#     return replace_substr(result, substring)
#
#
# remove_string = input()
# text = input()
# print(replace_substr(text, remove_string))
