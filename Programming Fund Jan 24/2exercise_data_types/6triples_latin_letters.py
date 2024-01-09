number = int(input())

for first in range(97, number + 97):
    for second in range(97, number + 97):
        for third in range(97, number + 97):
            print(f'{chr(first)}{chr(second)}{chr(third)}')