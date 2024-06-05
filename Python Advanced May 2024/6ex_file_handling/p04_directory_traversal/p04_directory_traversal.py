import os

files = {}
directory = input()  # '.'   '../'


def get_files(folder, level):
    if level < 0:
        return
    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            ext = os.path.splitext(element)[1]
            if ext not in files:
                files[ext] = []
            files[ext].append(element)
        else:
            get_files(f, level - 1)
            # get_files(f, level - 1 if level != -2 else -2)    # in case dummy -2 is used - to obtain max possible lvl


get_files(directory, 1)     # choose number of levels/directory depth
# get_files(directory, -2)    # dummy number. -1 is used for return, so could be any other unused number, for max depth

with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
    for extension, file_names in sorted(files.items()):
        output_file.write(f'{extension}\n')
        for file_name in sorted(file_names):
            output_file.write(f'- - - {file_name}\n')


# Method 2
# files = {}
# directory = '../'
#
# for element in os.listdir(directory):
#     f = os.path.join(directory, element)
#     if os.path.isfile(f):
#         ext = element.split('.')[-1]
#         if ext not in files:
#             files[ext] = []
#         files[ext].append(element)
#     else:   # elif os.path.isdir(f):
#         for el in os.listdir(f):
#             filepath = os.path.join(f, el)
#             if os.path.isfile(filepath):
#                 ext = el.split('.')[-1]
#                 if ext not in files:
#                     files[ext] = []
#                 files[ext].append(el)
#
# with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
#     for extension, file_names in sorted(files.items()):
#         output_file.write(f'.{extension}\n')
#         for file_name in sorted(file_names):
#             output_file.write(f'- - - {file_name}\n')


# Method 3
# def extract_files_and_extensions(dir_path, sub_levels):
#     """
#     A recursive function that receives a dir path and the level limit of subdirectories which have to be processed.
#     The goal of the recursion is to limit the levels of the sub folders that need to be processed.
#     All files in these directories are classified according to their extensions. Results are stored in a dictionary.
#     """
#
#     # We create a list of all items in the directory.
#     current_directory = os.listdir(dir_path)
#
#     # We loop through each item and check is a file or a folder.
#     # If it's a folder, we use recursion to process its content to the set limit.
#     for item in current_directory:
#         if len(item.split(".")) == 1:
#             if sub_levels != 0:  # We set the depth of the recursion
#                 sub_dir_path = f"{dir_path}/{item}"
#                 extract_files_and_extensions(sub_dir_path, sub_levels - 1)  # We reduce the level for the recursion
#
#     # If the item is a file, we add it to our dictionary.
#         else:
#             file_extension = item.split('.')[-1]
#
#             if file_extension not in extensions:
#                 extensions[file_extension] = []
#
#             extensions[file_extension].append(item)
#
#
# # We receive the path through user input and set the limit of sub folder levels.
# # We'll store the extensions in a dictionary.
# directory_path = input()
# allowed_levels = 1
# extensions = {}
#
# # We call the function to process the directories and files at the given path.
# extract_files_and_extensions(directory_path, allowed_levels)
#
# # After we have all extensions, we sort them alphabetically.
# sorted_extensions = sorted(extensions.items(), key=lambda x: (x[0]))
#
# # Create an empty string to store the final result and then loop through our dictionary to add extensions and files.
# result = ""
# for extension, files in sorted_extensions:
#     result += f".{extension}\n"
#     # The file names for each extension are also sorted alphabetically before we add them to the result string.
#     for file in sorted(files):
#         result += f"- - - {file}\n"
#
# # We write the result to a file.
# with open("report.txt", "w") as file:
#     file.write(result)
