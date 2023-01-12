import os

# os.rename(path1, path2)
# os.rename('input.txt','input_new.txt')
# os.rename('dir1','dir1_new')

# # os.mkdir() - create a new folder or directory
# def create_dir(path):
#    if not os.path.exists(path):
#       os.mkdir(path)
# create_dir('new_dir')

# def create_dir(path):
#    if not os.path.exists(path):
#       os.makedirs(path)
# path = 'grandfather/father/son/grandson'
# create_dir(path)


def safe_rename(path1):
   path2 = 'new_new.txt'
   if os.path.exists(path1):
      os.rename(path1,path2)
path1 = input()
safe_rename(path1)

