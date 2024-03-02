def is_palindrome(numbers):
    if numbers[::-1] == numbers:
        return True
    else:
        return False


sequence = list(map(str, input().split(', ')))
for num in sequence:
    print(is_palindrome(num))


# def is_palindrome(num):
#     return num == num[::-1]
# def palindrome_function(lst):
#     return '\n'.join(['True' if is_palindrome(num) else 'False' for num in lst])
#
# list_palindromes = list(map(str, input().split(', ')))
# print(palindrome_function(list_palindromes))