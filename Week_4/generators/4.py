from math import sqrt as s
def squares(a,b):
   for i in range(int(s(a)),int(s(b))+1):
      yield i*i

a = int(input())
b = int(input())

for item in squares(a,b):
   print(item)
