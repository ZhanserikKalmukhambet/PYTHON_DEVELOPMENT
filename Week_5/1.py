import re

s = input()

match = re.search(r"ab*",s)

if match:
   print('Pattern exists')
else:
   print('Not found')
   