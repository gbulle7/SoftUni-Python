# string = input()
# stack = []
# for char in range(len(string) - 1, -1, -1):
#     stack.append(string[char])
# print("".join(stack))


text = list(input())
stack = []
for i in range(len(text)):
    stack.append(text.pop())
print("".join(stack))


# text = input()
# print(text[::-1])


# text = list(input())
# while text:
#     print(text.pop(), end="")