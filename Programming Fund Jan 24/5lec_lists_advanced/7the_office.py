happiness = input().split()
factor = int(input())

happiness_factored = list(map(lambda x: int(x) * factor, happiness))
# happiness_factored = [int(x) * factor for x in happiness]

filtered = list(filter(lambda y: y >= (sum(happiness_factored) / len(happiness_factored)), happiness_factored))

if len(filtered) >= len(happiness_factored) / 2:
    print(f'Score: {len(filtered)}/{len(happiness_factored)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(happiness_factored)}. Employees are not happy!')


# def check_employee_happiness():
#     happiness_list = list(map(int, input().split()))
#     happiness_factor = int(input())
#
#     improved_happiness = [h * happiness_factor for h in happiness_list]
#
#     average_happiness = sum(improved_happiness) / len(improved_happiness)
#
#     happy_count = sum(h >= average_happiness for h in improved_happiness)
#
#     total_count = len(improved_happiness)
#
#     message = 'happy' if happy_count >= total_count / 2 else 'not happy'
#     result = f'Score: {happy_count}/{total_count}. Employees are {message}!'
#
#     return result
#
#
# result = check_employee_happiness()
# print(result)