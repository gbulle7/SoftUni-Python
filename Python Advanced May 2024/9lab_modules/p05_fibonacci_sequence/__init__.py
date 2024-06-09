from fibonacci_sequence import fibonacci, locate

while True:
    command = input().split()
    cmd = command[0]
    if cmd == 'Stop':
        break
    num = int(command[-1])
    if cmd == 'Create':
        print(fibonacci(num))
    elif cmd == 'Locate':
        print(locate(num))
