happiness = input().split()
factor = int(input())

happiness_factored = list(map(lambda x: int(x) * factor, happiness))

filtered = list(filter(lambda y: y >= (sum(happiness_factored) / len(happiness_factored)), happiness_factored))

if len(filtered) >= len(happiness_factored) / 2:
    print(f'Score: {len(filtered)}/{len(happiness_factored)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(happiness_factored)}. Employees are not happy!')
