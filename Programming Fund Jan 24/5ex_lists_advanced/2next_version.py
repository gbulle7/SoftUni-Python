def next_version(current_version):
    version = 2
    current_version[version] += 1
    if current_version[version] > 9:
        current_version[version] = 0
        current_version[version - 1] += 1
        if current_version[version - 1] > 9:
            current_version[version - 1] = 0
            current_version[version - 2] += 1

    new_version = '.'.join([str(next_v) for next_v in current_version])
    return new_version


initial_version = list(map(int, input().split('.')))
print(next_version(initial_version))
