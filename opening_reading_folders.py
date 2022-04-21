import os
import shutil
import send2trash

# f = open('practice.txt', 'w+')
#
# f.write('This is a test string')

# os.getcwd()
#
# print(os.listdir('/home/ivansidorov/Altinity/PrivateProjects'))

# shutil.move('practice.txt', '/home/ivansidorov/Altinity/PrivateProjects')

# send2trash.send2trash('../practice.txt')

file_path = '/home/ivansidorov/Altinity/UdemyCourse/Complete-Python-3-Bootcamp/12-Advanced\ Python\ Modules/Example_Top_Level'

for folder, sub_folders,files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    # print('\n')
    # print('The sub_folders are: ')
    # for sub_folder in sub_folders:
    #     print(f"{sub_folder}")

print(os.walk(file_path))
