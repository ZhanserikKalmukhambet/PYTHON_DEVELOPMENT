l = ['Almat', 'Zhanserik', 'Ansar', 'Rauan'] # list of participants
x = frozenset(l)
# x[1] = 'Dimash'

#####################################

class Person:
  name = "John"
  age = 36
  country = "Norway"
x = getattr(Person,'name',)
print(x)

#####################################

class Pet:
   name = 'Simba'
   color = 'brown'
print(hasattr(Pet,'name'))
print(hasattr(Pet,'color'))
print(hasattr(Pet,'age'))

#####################################

a = int(input())
hex_format = hex(a)
print(hex_format[2:])

#####################################

class Person:
   name = 'John'
   age = 21
class Student(Person):
   id = '21BD308036'
print((issubclass(Student,Person)))