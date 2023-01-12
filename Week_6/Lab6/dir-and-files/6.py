import os

path = os.mkdir('26_txt_files')

os.chdir('26_txt_files')

for i in range(26):
   with open(f'{chr(i+65)}.txt', 'x', encoding='UTF-8') as f:
      f.write(f'№ {i+1} file is created!')





