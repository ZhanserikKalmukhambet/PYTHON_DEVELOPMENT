import re

def to_snake(txt):
   t = ""
   for i in range(len(txt)):
      t += txt[i]
      if txt[i].isupper():
         t += txt[i].lower()
         
   print(re.sub(r'[A-Z]','_',t))
         

s = input()
to_snake(s)

# camelStringCase ==> camel_string_case