number = int(input())
message = ''

for _ in range(number):
    num = int(input())
    if num == 88:
        message = 'Hello'
    elif num == 86:
        message = 'How are you?'
    elif num < 88:
        message = 'GREAT!'
    else:
        message = 'Bye.'
    print(message)