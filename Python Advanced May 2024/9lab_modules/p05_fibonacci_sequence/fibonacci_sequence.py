fib_seq = []


def fibonacci(n):
    global fib_seq
    fib_seq = []
    last_num = 0
    next_num = 1

    for i in range(n):
        fib_seq.append(last_num)
        last_num, next_num = next_num, last_num + next_num

    return ' '.join(map(str, fib_seq))


def locate(n):
    if n in fib_seq:
        return f'The number - {n} is at index {fib_seq.index(n)}'
    return f'The number {n} is not in the sequence'
