resources = {}

while True:
    resource = input()

    if resource == 'stop':
        break

    quantity = int(input())

    if resource not in resources:
        resources[resource] = 0

    resources[resource] += quantity


for k, v in resources.items():
    print(f'{k} -> {v}')
