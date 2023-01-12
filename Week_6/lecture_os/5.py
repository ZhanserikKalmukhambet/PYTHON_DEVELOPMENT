import os
# os.walk() ==> return all roots, files, directories

# base_url = os.getcwd()
# for root,dirs,files in os.walk(base_url):
#    print(root,dirs,files)

path = 'C:\Programming Principles II\PP2_LAB\Week_4'
for root,dirs,files in os.walk(path):
   print(root)
   print('ALL DIRECTORIES:')
   for dir in dirs:
      print(dir)
   print('All files:')
   for file in files:
      print(file)

