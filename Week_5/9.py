import re

def check(s):
   t = ''
   for i in range(len(s)):
      if s[i].isupper():
         t += '_'
         t += s[i]
      else:
         t += s[i]
   return t

s = input()

txt = check(s)

l = re.split(r'_',txt)

for i in l:
   print(i,end=' ')