first_number_limit = int(input())
second_number_limit = int(input())
third_number_limit = int(input())

for num1 in range(1, first_number_limit + 1):
    for num2 in range(2, second_number_limit + 1):
        if num2 % 2 == 0 and num2 != 2:
            continue
        for num3 in range(1, third_number_limit + 1):
            if num1 % 2 == 0 and num3 % 2 == 0 and num2 <= 7:
                print(f"{num1} {num2} {num3}")