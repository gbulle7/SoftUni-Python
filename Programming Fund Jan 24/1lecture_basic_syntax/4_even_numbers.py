total_numbers = int(input())

for _ in range(total_numbers):
    number = int(input())
    if number % 2 != 0:
        print(str(number) + ' is odd!')
        break
else:
    print('All numbers are even.')