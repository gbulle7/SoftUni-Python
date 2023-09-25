first_pair = int(input())
second_pair = int(input())
first_end_num = int(input())
second_end_num = int(input())
first_end = first_pair + first_end_num
second_end = second_pair + second_end_num

for first_num in range(first_pair, first_end + 1):
    for second_num in range(second_pair, second_end + 1):
        is_prime = True
        for num1 in range(2, first_num):
            if first_num % num1 == 0:
                is_prime = False
                break
        if not is_prime:  # not to waste resources for the second pair for loop since if the first isn't prime, not necessary to check the second pair
            break
        for num2 in range(2, second_num):
            if second_num % num2 == 0:
                is_prime = False
                break
        if is_prime:
            print(f'{first_num}{second_num}')
