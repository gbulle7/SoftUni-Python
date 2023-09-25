import math

n = int(input())
oddmax = -math.inf
oddmin = math.inf
oddsum = 0
evenmax = -math.inf
evenmin = math.inf
evensum = 0

for number in range(1, n + 1):
    current_number = float(input())
    if number % 2 == 0:
        if current_number > evenmax:
            evenmax = current_number
        if current_number < evenmin:
            evenmin = current_number
        evensum += current_number
    else:
        if current_number > oddmax:
            oddmax = current_number
        if current_number < oddmin:
            oddmin = current_number
        oddsum += current_number

print(f'OddSum={oddsum:.2f},')
if oddmin == math.inf:
    print('OddMin=No,')
else:
    print(f'OddMin={oddmin:.2f},')
if oddmax == -math.inf:
    print('OddMax=No,')
else:
    print(f'OddMax={oddmax:.2f},')
print(f'EvenSum={evensum:.2f},')
if evenmin == math.inf:
    print('EvenMin=No,')
else:
    print(f'EvenMin={evenmin:.2f},')
if evenmax == -math.inf:
    print('EvenMax=No')
else:
    print(f'EvenMax={evenmax:.2f}')
