def perfect_number(num):
    # sum_divisors = sum(divisor for divisor in range(1, num) if num % divisor == 0)
    sum_divisors = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sum_divisors += divisor
    if sum_divisors == num:
        return 'We have a perfect number!'
    else:
        return 'It\'s not so perfect.'
    # return 'We have a perfect number!' if sum_divisors == num else 'It\'s not so perfect.'


number = int(input())
print(perfect_number(number))
