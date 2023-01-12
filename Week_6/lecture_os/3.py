import os  # operational system

# os.path.exists(path) ==> return True or False
# os.remove(path) ==> delete the file
# os.path.isdir(path) ==> существует ли папка ?
# os.path.isfile(path) ==> существует ли файл ?

path = 'input2.txt'
if os.path.exists(path):
   print('This path exists')
   os.remove(path)
   print('This file is deleted.')
else:
   print('No')

path_dir = 'C:\Programming Principles II\PP2_LAB\Week_6\Lab6'
if os.path.isdir(path_dir):
   print('Yes')
else:
   print('No')

path_file = 'C:\Programming Principles II\PP2_LAB\Lab6\input.txt'
print('Yes') if os.path.isfile(path_file) else print('No')

