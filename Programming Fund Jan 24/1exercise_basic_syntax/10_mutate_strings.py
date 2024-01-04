word = input()
second_word = input()
new_string = ""

for i in range(len(word)):
    new_string = second_word[:i + 1] + word[i + 1:]
    if word[i] != second_word[i]:
        print(new_string)

# s1 = input()
# s2 = input()
#
# for i in range(len(s1)):
#    if s1[i] != s2[i]:
#        s1 = s1[:i] + s1[i:i + 1].replace(s1[i], s2[i], 1) + s1[i + 1:]
#        print(s1)

# with List
# text1 = input()
# text2 = input()
# transform_list = list(text1)
#
# for letter in range(len(text1)):
#     if transform_list[letter] != text2[letter]:
#         transform_list[letter] = text2[letter]
#         print("".join(transform_list))

# without slicing notation
# first = input()
# second = input()
# new = ""
# add = ""
#
# for i in range(0, len(first)):
#     if first[i] == second[i]:
#         add = first[i]
#         new += add
#     else:
#         add = second[i]
#         new += add
#         new1 = new
#         for j in range(i + 1, len(first)):
#             new1 += first[j]
#         print(new1)