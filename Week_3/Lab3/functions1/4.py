def filter_prime(x):
   for i in range(2,x):
      if x%i==0:
         return False
   return True

l = list(map(int,input().split()))
for num in l:
   if filter_prime(num):
      print(num,end=' ')