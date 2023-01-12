import re

s = input()

match = re.findall(r'[A-Z][a-z]+',s)

if match:
   print('Pattern exists')
   for pattern in match:
      print(pattern)
else:
   print('Not found')