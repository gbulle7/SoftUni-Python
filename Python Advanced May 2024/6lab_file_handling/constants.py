from os import path
# from os.path import abspath, dirname

# ABSOLUTE_PROJECT_PATH = os.path.abspath(__file__ + "/../..")
ABSOLUTE_PROJECT_PATH = path.dirname(path.dirname(path.abspath(__file__)))   # same as above
# print(ABSOLUTE_PROJECT_PATH)
