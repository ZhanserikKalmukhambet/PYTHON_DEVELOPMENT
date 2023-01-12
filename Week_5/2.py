import re

s = input()

match = re.findall(r"ab{2,3}",s)

if match:
   print('Pattern exists')
else:
   print('Not found')

