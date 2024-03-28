text = input()
rage_message = ""
repetitions = ""
sub_string = ""
for index in range(len(text)):
    if not text[index].isdigit():  # non-numeric symbol
        sub_string += text[index].upper()
    else:  # number of repetitions
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        rage_message += sub_string * int(repetitions)
        repetitions = ""
        sub_string = ""
print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)


# import re
#
# string = input()
#
# list_of_chars = re.findall(r"\D+", string)
# list_of_digit = re.findall(r"\d+", string)
# new_string_list = [x.upper() * int(y) for x, y in zip(list_of_chars, list_of_digit)]
# new_string = "".join(new_string_list)
# number_of_unique_symbols = len(set(new_string))
#
# print(f"Unique symbols used: {number_of_unique_symbols}")
# print(new_string)
