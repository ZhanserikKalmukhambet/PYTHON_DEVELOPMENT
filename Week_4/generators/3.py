def gen(n):
   i = 0
   while i!=n+1:
      if i%3==0 and i%4==0:
         yield i
      i+=1

n = int(input())

l = []
for item in gen(n):
   l.append(item)

it = iter(l)

for num in it:
   print(num)