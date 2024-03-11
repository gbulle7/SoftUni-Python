def positive(nums):
    positive_numbers = [str(num) for num in nums if num >= 0]
    return f"Positive: {', '.join(positive_numbers)}"


def negative(nums):
    negative_numbers = [str(num) for num in nums if num < 0]
    return f"Negative: {', '.join(negative_numbers)}"


def even(nums):
    even_numbers = [str(num) for num in nums if num % 2 == 0]
    return f"Even: {', '.join(even_numbers)}"


def odd(nums):
    odd_numbers = [str(num) for num in nums if num % 2 != 0]
    return f"Odd: {', '.join(odd_numbers)}"


numbers = list(map(int, input().split(', ')))
print(positive(numbers))
print(negative(numbers))
print(even(numbers))
print(odd(numbers))
