import os

path = 'example_2.txt'

# check the readability
try:
   with open(path, 'r', encoding='UTF-8') as f:
      for line in f:
         print(line)
except Exception as e:
   print(str(e))

# check the writability
if os.path.exists(path):
   with open(path,'w') as f:
      f.write('Delete all the content\n')
      f.write('And Write a new text\n')
      f.write('New content is available')

# check the executability
if os.path.exists(path):
   with open(path,'a') as f:
      f.write('This file is executable!')




