# Function is callable, jsut variable is not callable
def x():
   a = 5
print(callable(x))

####################################

x = compile('print(55)\nprint(77)', 'test', 'exec')
exec(x)

####################################

x = complex(3, 5)
print(x)

####################################

class Student:
   name = 'Jones'
   age = 17
   id = '21BD308036'
delattr(Student,'age') #  deleted the attribute to use 
p = Student()
print(p.age) # it returns a False



