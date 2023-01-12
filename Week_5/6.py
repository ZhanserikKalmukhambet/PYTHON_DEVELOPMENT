import re

s = input()

txt = re.sub(r'[ ]|[,]|[.]' , ':' , s)

print(txt)