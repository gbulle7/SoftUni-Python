from os import remove
new_file_to_delete = open('new_file_to_del.txt', 'w')
new_file_to_delete.write('Test')
new_file_to_delete.close()

try:
    remove('new_file_to_del.txt')
except FileNotFoundError:
    print("File already deleted or doesn't exist!")

# path = os.path.join('6lab_file_handling', 'new_file_to_del.txt')  # if script/main file in main directory
# if os.path.exists(path):
#     os.remove(path)
# else:
#     print('File already deleted')
