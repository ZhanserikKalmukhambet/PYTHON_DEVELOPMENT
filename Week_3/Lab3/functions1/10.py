def unique(l):
   new = []
   for num in l:
      if not num in new:
         new.append(num)
      else:
         pass
   return new

l = list(map(int,input().split()))
print(unique(l))