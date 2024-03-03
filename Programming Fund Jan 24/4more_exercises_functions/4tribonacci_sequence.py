number = int(input())


def tribonacci_sequence(num):
    sequence = [1]
    for i in range(1, num):
        if len(sequence) < 3:
            sequence.append(i)
        else:
            sequence.append(sum(sequence[-3:]))
    return ' '.join([str(num) for num in sequence])


print(tribonacci_sequence(number))

# number_lines = int(input())
#
#
# def tribonacci(number):
#     tribo_list = [1, 0, 0]
#     for num in range(number):
#         next_num = sum(tribo_list)
#         print(next_num, end=' ')
#         tribo_list.append(next_num)
#         tribo_list.pop(0)
#
#
# tribonacci(number_lines)
