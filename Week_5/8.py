import re

s = input()

l = re.split(r'[A-Z]+',s)

for word in l:
   print(word)