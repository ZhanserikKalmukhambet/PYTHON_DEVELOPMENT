import re

# def convert(txt):

#    l = re.split("[_]", txt)
   
#    print(l[0], end="")
#    for i in range(1, len(l)):
#       print(l[i].capitalize(), end="")

# s = input()
# convert(s)

s = input()

l = re.split('\W+', s)

print(l)