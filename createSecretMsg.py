#
#
#
# this code renames all the files in a particular directory
# by stripping out all numeric characters
#
import os

def rename_files():
#
# (1) get file names
    saved_path = os.getcwd()
    cwd = "/Users/devimahendran/Desktop/Python_lessons/Lesson2/random_dirs"
    file_list = os.listdir(cwd)
    print(file_list)
    os.chdir(cwd)
# (2) for each file_name
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
#
#
rename_files()
