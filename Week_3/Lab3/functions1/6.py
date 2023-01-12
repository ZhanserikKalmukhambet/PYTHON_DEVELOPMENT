def reverse(l):
   res = []
   for i in range(len(l)-1,-1,-1):
      res.append(l[i])
   return res

l = list(map(str,input().split()))
new = reverse(l)
for words in new:
   print(words,end=' ')
