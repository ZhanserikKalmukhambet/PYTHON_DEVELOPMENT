import os
base_url = os.getcwd()
for target in os.listdir('.'):         # '.' текущая папка
   target_path = os.path.join(base_url,target)
   if os.path.isfile(target_path):
      print('FILE:', f'{target_path}')
      print()
   else:
      print('DIR:', f'{target_path}')
      for f in os.listdir(target_path):
         f_path = os.path.join(base_url,target,f)
         if os.path.isdir(f_path):
            print('      Dir:',f'{f_path}')
         else:
            print('      File:',f'{f_path}')
      print()

