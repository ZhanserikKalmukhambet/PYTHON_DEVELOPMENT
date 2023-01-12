import os

path = input('Enter or copy\paste the path of one of your projects:\n')

if os.path.exists(path):
   print(path)
   for target in os.listdir(path):
      print(target)
else:
   print('Entered path does not exist. Try next time!')


