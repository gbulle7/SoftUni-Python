words = input().split()
palindrome = input()
palindromes = []

for word in words:
    if word[::-1] == word:  # if word == ''.join(reversed(word)):
        palindromes.append(word)

print(palindromes)
count = palindromes.count(palindrome)
print(f'Found palindrome {count} times')

# words = input().split(' ')
# palindrome = input()
# palindromes_list = [word for word in words if word == word[::-1]]
#
# found_palindromes = [word for word in words if word == palindrome]
# palindrome_counter = len(found_palindromes)
#
# print(palindromes_list)
# print(f"Found palindrome {palindrome_counter} times")