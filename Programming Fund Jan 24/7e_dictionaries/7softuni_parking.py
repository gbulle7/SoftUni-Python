commands = int(input())
parking = {}

for _ in range(commands):
    command = input().split()
    action, username = command[0], command[1]

    if action == 'register':
        license_plate = command[2]
        if username in parking:
            print(f'ERROR: already registered with plate number {license_plate}')
            continue
        else:
            parking[username] = license_plate
            print(f'{username} registered {license_plate} successfully')

    elif action == 'unregister':
        if username not in parking:
            print(f'ERROR: user {username} not found')
        else:
            parking.pop(username)
            print(f'{username} unregistered successfully')

for user, vehicle in parking.items():
    print(f'{user} => {vehicle}')
