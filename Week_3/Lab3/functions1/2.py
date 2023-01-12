def convert(x):
   return (x-32)*(5/9)

F = int(input())
C = round(convert(F),2)
print(C)