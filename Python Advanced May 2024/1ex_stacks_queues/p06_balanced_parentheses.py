# sequence = input()
# stack = []
# is_valid = True
# for bracket in sequence:
#     if bracket == "{" or bracket == "(" or bracket == "[":
#         stack.append(bracket)
#     else:
#         if not stack:
#             is_valid = False
#             break
#         last_bracket = stack.pop()
#         if bracket == "}" and last_bracket != "{":
#             is_valid = False
#             break
#         elif bracket == ")" and last_bracket != "(":
#             is_valid = False
#             break
#         elif bracket == "]" and last_bracket != "[":
#             is_valid = False
#             break
# if is_valid:
#     print("YES")
# else:
#     print("NO")

from collections import deque
expression = deque(input())
opening_brackets = '([{'
closing_brackets = ')]}'
counter = 0
while expression and counter < len(expression) / 2:
    if expression[0] not in opening_brackets:
        break
    index = opening_brackets.index(expression[0])
    if expression[1] == closing_brackets[index]:
        expression.popleft()
        expression.popleft()
        expression.rotate(counter)
        counter = 0
    else:
        expression.rotate(-1)
        counter += 1
if not expression:
    print("YES")
else:
    print("NO")
