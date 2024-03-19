words = input().split()

dictionary = {}
# word_list = []

for word in words:
    word = word.lower()
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')

# for word in dictionary:
#     if dictionary[word] % 2 != 0:
#         # print(word, end=' ')
#         word_list.append(word)
#
# print(' '.join(word_list))



# sequence = input().split(' ')
#
# final_dic = {}
# for element in sequence:
#     counter = 0
#     word = element.lower()
#     for curr_element in sequence:
#         if curr_element.lower() == word:
#             counter += 1
#     if counter % 2 != 0:
#         final_dic[element.lower()] = element
#
# print(' '.join(final_dic))