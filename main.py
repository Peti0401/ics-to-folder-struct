import dirmaker


# Main
ics_file_path = input("Enter the path of the ics file: ")
root_dir_path = input("Enter the path of the enclosing directory: ")

# Reading sub-directory input
sub_dirs = []
print("(All sub directories should be relative to ", root_dir_path, ")")
answer = input("Would you like to specify sub-directories? (yes/no) - ")
while answer.__eq__("yes"):
    sub_dir = input("Specify sub-directory: ")
    sub_dirs.append(sub_dir)
    answer = input(
        "Would you like to specify more sub-directories? (yes/no) - ")

# Reading pre-made files input
sub_dir_files = []
answer = input("Would you like to specify files? (yes/no) - ")
while answer.__eq__("yes"):
    file_name = input("Specify file name: ")
    sub_dir_files.append(file_name)
    answer = input("Would you like to specify more files? (yes/no) - ")

dirmaker.construct_directories(
    ics_file_path, root_dir_path, sub_dirs, sub_dir_files)
print("Directories created!")
