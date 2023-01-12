def gen(n):
   while n!=-1:
      yield n
      n-=1

n = int(input())
for item in gen(n):
   print(item,end=' ')