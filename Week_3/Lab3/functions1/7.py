def has_33(l):
   for i in range(len(l)-1):
      if l[i]==l[i+1]==3:
         return True
         exit()
   return False

l = list(map(int,input().split()))
print(has_33(l))