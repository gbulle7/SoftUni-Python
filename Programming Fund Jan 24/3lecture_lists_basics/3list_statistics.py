number = int(input())
positives = []
negatives = []

for _ in range(number):
    num = int(input())
    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}\n'
      f'Sum of negatives: {sum(negatives)}')

