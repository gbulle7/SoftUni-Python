def next_version(current_version):
    version = 2
    current_version[version] += 1
    if current_version[version] > 9:
        current_version[version] = 0
        current_version[version - 1] += 1
        if current_version[version - 1] > 9:
            current_version[version - 1] = 0
            current_version[version - 2] += 1

    new_version = '.'.join(str(next_v) for next_v in current_version)
    return new_version


initial_version = list(map(int, input().split('.')))
print(next_version(initial_version))


# version = [int(digit) for digit in input().split('.')]
# version[-1] += 1
# for index in range(len(version), 0, -1):
#     if version[index] > 9:
#         version[index] = 0
#         version[index - 1] += 1
# print('.'.join(str(digit) for digit in version))


# current_version = ''.join(input().split('.'))
# current_version = f'{int(current_version) + 1}'
# next_version = []
# for digit in current_version:
#     next_version.append(digit)
# print('.'.join(next_version))

