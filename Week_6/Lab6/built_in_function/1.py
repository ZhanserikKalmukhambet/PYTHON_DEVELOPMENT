def result(l):
   res = 1
   for x in l:
      res *= x
   return res

l = list(map(int,input().split()))
print(result(l))
