# class Person():
#    name = 'Jones'
#    age = 17
#    gpa = 3.86
#    def show(self):
#       print(f'{self.name} -- {self.age} -- {self.gpa}')

# p = Person()
# p.age = 20 # change the value
# print(p.name, p.age, p.gpa)
# p.show()


# class Students:
#    def __init__(self,name,age,faculty,gpa):
#       self.name = name
#       self.age = age
#       self.faculty = faculty
#       self.gpa = gpa
#    def show(self):
#       print(self.name,self.age,self.faculty,self.gpa,end=' ')
#    def __str__(self):
#       print(self.name)

# s1 = Students('Jones',17,'FIT',3.86)
# s2 = Students('Sultan',18,'Buisness',3.33)
# print(s1.show())
# print(s2.show())
# print(s1)


class Person():
   def __init__(self,name,surname,age):
      self.name = name
      self.surname = surname
      self.age = age
   def __str__(self):
      return f'{self.name} {self.surname} ==> {self.age}'

class Student(Person):
   def __init__(self,name,surname,age,gpa,id):
      super().__init__(name,surname,age)
      self.gpa = gpa
      self.id = id
   def __str__(self):
      return f'{super().__str__()} ==> {self.gpa} ==> {self.id}'

s = Student('Jones','Kalmukhambet',17,3.86,'21B30108')
print(s)

class Employee(Person):
   def __init__(self,name,surname,age,salary,time):
      super().__init__(name,surname,age)
      self.salary = salary
      self.time = time
   def __str__(self):
      return f'{super().__str__()} ==> {self.salary} ==> {self.time}'

e = Employee('Rustem','Kasymov',41,'180k','9 hours')
print(e)


class Dog():
   def __init__(self,name,age,color):
      self.name = name
      self.age = age
      self.color = color
   def __str__(self):
      return f'{self.name} is {self.age} years old. And color of this pet {self.color}'

d = Dog('Laika', 1,'white-brown')
print(d)


