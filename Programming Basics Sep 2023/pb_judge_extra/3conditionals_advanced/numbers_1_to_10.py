# while loop
number = 1  # can be = 0 if line 5 is before line 4
while number < 11:  # can be number <= 10
    print(number)  # ^ if here is line 5 "number += 1"
    number += 1  # ^ if here is line 4 "print(number)

# for loop
# for number in range(1, 11):
#     print(number)