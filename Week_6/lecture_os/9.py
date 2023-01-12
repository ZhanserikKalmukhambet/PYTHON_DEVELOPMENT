import os

def show_all(path):
   for target in os.listdir(path):
      target_path = os.path.join(path,target)
      if os.path.isfile(target_path):
         print(f'File: {target_path}')
      else:
         print(f'Dir: {target_path}')
         show_all(target_path)

base_url = os.getcwd()
show_all(base_url)