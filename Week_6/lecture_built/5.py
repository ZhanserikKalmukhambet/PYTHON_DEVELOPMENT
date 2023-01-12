last = ['Kalmukhambet','Abay']
name = ['Zhanserik','Meirambek']
add = lambda l,n: l + ' ' + n
l = list(map(add,last,name))
print(l)

#################################

alph = ['a','b','c','d','e']
realph = reversed(alph)
for l in realph:
   print(l)

#################################

class Car:
   name = 'Porsche'
   color = 'red'
   price = '12m$'
setattr(Car,'price','11m$')
setattr(Car,'color','black')
get = Car()
print(get.price, get.color, get.name)

###################################

name = ['Jones','Dima','Erin']
surname = ['Kalmukhambet','Erbobek','Arystanbek']
fatherlands = ['Rustemuly', 'Rauanuly', 'Nurzhanuly']
together = list(zip(name,surname,fatherlands))
for info in together:
   for target in info:
      print(target,end=' ')
   print()