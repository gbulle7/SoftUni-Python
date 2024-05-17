# lines = int(input())
# stack = []
# final_stack = []
# for _ in range(lines):
#     query = input().split()
#     command = query[0]
#     if command == "1":
#         num = int(query[1])
#         stack.append(num)
#     elif stack:
#         if command == "2":
#             if stack:
#                 stack.pop()
#         elif command == "3":
#             print(max(stack))
#         elif command == "4":
#             print(min(stack))
#
# for _ in range(len(stack)):
#     final_stack.append(stack.pop())
# print(", ".join(map(str, final_stack)))


n = int(input())
stack = []
functions = {
    '1': lambda x: stack.append(int(x)),
    '2': lambda: stack.pop() if stack else None,
    '3': lambda: print(max(stack)) if stack else None,
    '4': lambda: print(min(stack)) if stack else None
}

for _ in range(n):
    command = input().split()
    functions[command[0]](*command[1:])
print(*reversed(stack), sep=", ")


# With Deque
# from _collections import deque
#
# stack = deque()
#
# number_of_queries = int(input())
#
# for i in range(number_of_queries):
#     query = input().split(' ')
#     query_type = query[0]
#     if query_type == "1":
#         query_element = query[1]
#         stack.appendleft(int(query_element))
#
#     elif query_type == "2":
#         if len(stack) == 0:
#             pass
#         else:
#             stack.popleft()
#
#     elif query_type == "3":
#         if len(stack) == 0:
#             pass
#         else:
#             print(max(stack))
#
#
#     elif query_type == "4":
#         if len(stack) == 0:
#             pass
#         else:
#             print(min(stack))
#
# stack = list(map(lambda x: str(x), stack))
#
# print(", ".join(stack))