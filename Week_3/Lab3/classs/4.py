from math import sqrt as s

class Point():
   def __init__(self,x1,y1,x2,y2):
      self.x1 = x1
      self.y1 = y1
      self.x2 = x2
      self.y2 = y2

   def show(self):
      print(f'A = ({self.x1},{self.y1})\nB = ({self.x2},{self.y2})')
      print()

   def move(self):
      x3,y3 = map(int,(input().split()))
      print(f'point A is moved to ({self.x1+x3},{self.y1+x3}) by ({x3},{y3})')
      print(f'point A is moved to ({self.x2+x3},{self.y2+x3}) by ({x3},{y3})')
      print()

   def dist(self):
      dist = round(s((self.x2-self.x1)**2 + (self.y2-self.y1)**2),3)
      print(f'Distance between A and B : {dist}')
      print()

# x1,y1 = map(int,input('Enter the coordinates of point A:\n').split())
# x2,y2 = map(int,input('Enter the coordiantes of point B:\n').split())

p1 = Point(x1,y1)
p2 = Point(x2,y2)

p1.dist(p2)

p.show()
p.move()
p.dist()
