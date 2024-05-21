first_seq = {int(x) for x in input().split()}
second_seq = {int(x) for x in input().split()}


def add_seq(seq, nums):
    if seq == 'First':
        first_seq.update(nums)
    elif seq == 'Second':
        second_seq.update(nums)


def remove_seq(seq, nums):
    if seq == 'First':
        seq = first_seq
    elif seq == 'Second':
        seq = second_seq
    for num in nums:
        if num in seq:
            seq.remove(num)


def check_subset():
    seq1 = first_seq
    seq2 = second_seq
    # print((seq1.issubset(seq2) or seq2.issubset(seq1))
    if seq1.issubset(seq2) or seq2.issubset(seq1):
        print('True')
    else:
        print('False')


commands = {
    'Add': add_seq,
    'Remove': remove_seq,
    'Check': check_subset
}

n = int(input())
for _ in range(n):
    current_command = input().split()
    cmd, sequence = current_command[0], current_command[1]

    # cmd = current_command[0] + ' ' + current_command[1]
    # numbers = [int(x) for x in current_command[2:]]
    # if cmd == 'Add First':
    #   first_seq.update(numbers)
    # ... all cases (Add Second, Remove First, Remove Second, Check Seq)

    if not cmd == 'Check':
        numbers = set(map(int, current_command[2:]))
        commands[cmd](sequence, numbers)
    else:
        commands[cmd]()

print(*sorted(first_seq), sep=', ')
print(*sorted(second_seq), sep=', ')
# print(', '.join([str(x) for x in sorted(first_seq)]))
# print(', '.join([str(x) for x in sorted(second_seq)]))
