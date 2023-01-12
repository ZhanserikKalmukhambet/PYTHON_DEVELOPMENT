with open('input.txt','w') as f: # mode 'write' - delete all info in file and write new info
   f.write('hello world\n')
   f.write('how are you?\n')
   f.write('I am happy\n')

with open('input.txt','a') as f: # add new information
   f.write('append new line\n')
   f.write('do not delete old information\n')

with open('input2.txt','x') as f:
   f.write('create new mode\n')
   f.write('create new file\n')
   f.write('for another information\n')