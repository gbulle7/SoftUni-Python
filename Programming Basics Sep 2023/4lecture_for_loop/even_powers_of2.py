n = int(input())

for number in range(n + 1):
    if number % 2 == 0:
        print(2 ** number)


# n = int(input())
#
# number = 1
# for _ in range(0, n + 1, 2):    # step "2" - only even indexes; starting from "0", input "n" included as ending number "n+1" ## "_" variable, because no variable is used in the loop
#     print(number)  # firstly printing 1
#     number = number * 2 * 2

