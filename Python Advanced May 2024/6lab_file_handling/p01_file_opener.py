try:
    file = open('textfile.txt', 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')

# With absolute path /supposedly constants folder and abs_pj_path.py file created/
# import os
# from constants import ABSOLUTE_PROJECT_PATH
# path = os.path.join(ABSOLUTE_PROJECT_PATH, "6lab_file_handling", "textfile.txt")
# try:
#     open(path)
#     print('File found')
# except FileNotFoundError:
#     print('File not found')
