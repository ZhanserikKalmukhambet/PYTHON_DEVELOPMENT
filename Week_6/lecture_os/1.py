f = open('input.txt','r')

print(f)
print(f.read())

line1 = f.readline() # it reads rows one by one
line2 = f.readline()
print(line1, line2)

lines = f.readlines()
print(lines)

for line in f:
   print(line)

f.close()


# 2-variant
with open('input.txt','r') as f:
   for line in f:
      print(line)