s = input()
upper = 0
lower = 0
it = iter(s)
for letter in it:
   if 65 <= ord(letter) <= 90:
      upper += 1
   else:
      lower += 1
print(lower,upper)