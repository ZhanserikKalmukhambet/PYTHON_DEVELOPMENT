import re

s = input()

match = re.findall("[a-z]+_",s)

for pattern in match:
   print(pattern)