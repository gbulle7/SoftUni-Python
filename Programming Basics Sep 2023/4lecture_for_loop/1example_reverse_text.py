university = input()

for index in range(len(university)-1, -1, -1):
    print(index, '-', university[index])

# for letter in university[::-1]:     # slice notation
#     print(letter)

