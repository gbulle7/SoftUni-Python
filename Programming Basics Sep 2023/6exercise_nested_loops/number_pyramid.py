number = int(input())
counter = 1
completed = False

for row in range(1, number + 1):
    for col in range(row):
        if counter > number:
            completed = True
            break
        print(counter, end=' ')
        counter += 1
    if completed:
        break
    print()
