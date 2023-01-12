import os

# I'd choose to show all files and directories of week_6

def show_all(path):
   for target in os.listdir(path):
      target_path = os.path.join(path,target)
      if os.path.isfile(target_path):
         print(f'FILE: {target_path}')
      else:
         print(f'DIR: {target_path}')
         show_all(target_path)

path_week_6 = 'C:\Programming Principles II\PP2_LAB\Week_6'

show_all(path_week_6)

