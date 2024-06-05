from os import remove


def create_file(file_name):
    with open(file_name, 'w'):
        pass


def add_content(*args):
    file_name, content = args
    with open(file_name, 'a') as file:
        file.write(content + '\n')


def replace_data(*args):
    file_name, old_string, new_string = args
    try:
        with open(file_name) as file:
            text = file.read()
        text = text.replace(old_string, new_string)
        with open(file_name, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        print(f'An error occurred')


def delete_file(file_name):
    try:
        remove(file_name)
    except FileNotFoundError:
        print(f'An error occurred')


commands = {
    'Create': create_file,
    'Add': add_content,
    'Replace': replace_data,
    'Delete': delete_file
}

while True:
    command = input()
    if command == 'End':
        break
    command = command.split('-')
    commands[command[0]](*command[1:])

# Sample Input:
# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End


# Method 2
import os

while True:
    line = input()
    if line == 'End':
        break

    command, filename, *args = line.split('-')
    if command == 'Create':
        open(filename, 'w').close()
    elif command == 'Add':
        with open(filename, 'a') as f:
            f.write(f'{args[0]}\n')
    elif command == 'Replace':
        try:
            with open(filename, 'r+') as f:
                content = f.read()
                f.seek(0)
                f.truncate(0)
                f.write(content.replace(args[0], args[1]))
        except FileNotFoundError:
            print('An error occurred')
    elif command == 'Delete':
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print('An error occurred')
