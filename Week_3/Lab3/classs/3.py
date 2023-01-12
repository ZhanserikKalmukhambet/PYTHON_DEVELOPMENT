class Shape():
   def __init__(self,length,width):
      self.length = length
      self.width = width
   
class Rectangle(Shape):
   def area(self):
      print(self.length*self.width)

n = int(input())
m = int(input())
shape = Rectangle(n,m)
shape.area()