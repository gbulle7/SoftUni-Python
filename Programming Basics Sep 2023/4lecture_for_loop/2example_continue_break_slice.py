    # continue
# for number in range (1, 11):
#     if number == 6:
#         continue    # skip to next iteration of the loop (omitting the current operation, which is printing number 6)
#     print(number)

    # break
# for number in range (1, 11):
#     if number == 6:
#         break    # stops the operation of the loop when condition is met, any further iteration is broken (printing number 6 to 11 excluded)
#     print(number)

    # print format to print on one line
# for i in range(10):
#     print(i,i, sep="-", end=" ")     # print(i, sep="-", end="")
# print()   # return to default, so if there is next print, it won't be on same line

    # slicing notation !! different from slice() function !!
# a = range(100)
# ans = a[10:50:2]    # Slicing range function, can slice strings, etc..(sequence[start:stop:step])
# print(ans)

# method 1
# a = range(100)
# ans = a[10:50:2]
# for num in ans:
#     print(num)
#
# method 2
# a = range(100)
# b = slice(10, 50, 2)
# for num in a[b]:
#     print(num)

    # else statement in loop
# for letter in 'asfsdBdga':
#     if letter.lower() == 'b':  # make everything lowercase, so B will b
#         break
#     print(letter)
# else:
#     print('End of loop!')     # not executed because found letter "b" in the string and loop break