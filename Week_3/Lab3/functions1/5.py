from itertools import permutations
def to_list(s):
   l = []
   for letter in s:
      l.append(letter) 
   return l

def permm(l):
   perm = list(permutations(l))
   for tup in perm:
      for let in tup:
         print(let,end='')
      print()

s = input()
l = to_list(s)
permm(l)