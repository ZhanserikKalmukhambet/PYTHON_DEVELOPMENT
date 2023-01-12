def gen(n):
   i = 0
   while i!=n+1:
      if i%2==0:
         yield i
      i+=1

n = int(input())
for item in gen(n):
   print(item,end=' ')

