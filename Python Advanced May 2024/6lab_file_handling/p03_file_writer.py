new_file = open('my_first_file.txt', 'w')
# new_file = open('textfile.txt', 'x')  # "x" is like "w" but if the file exists, raises FileExistsError
new_file.write('I just created my first file!')
new_file.close()

file = open('my_first_file.txt', 'a')
file.write("\nThis is my first line\n")
file.write("I just created a new file\n")
file.write("It allows us to write in a particular file\n")
more_lines = ["This is how we can add multiple line\n",
              "We do it by adding the lines to a list\n",
              "And then use '.writelines()'\n"]
file.writelines(more_lines)
file.close()
