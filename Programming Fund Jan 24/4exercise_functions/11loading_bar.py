def loading_bar(percent):
    empty_bar = '[..........]'
    for pct in range(percent // 10):
        empty_bar = empty_bar.replace('.', '%', 1)
    if percent >= 100:
        print('100% Complete!')
        print(empty_bar)
    else:
        print(f'{percent}% {empty_bar}')
        print(f'Still loading...')
loaded_pct = int(input())
loading_bar(loaded_pct)

# def loading_bar(percent):
#     if percent == 100:
#         return f"100% Complete!\n[{'%' * 10}]"
#     return f"{percent}% [{'%' * (percent // 10)}{'.' * (10 - percent // 10)}]\nStill loading..."
#
#
# loading_percent = int(input())
# print(loading_bar(loading_percent))