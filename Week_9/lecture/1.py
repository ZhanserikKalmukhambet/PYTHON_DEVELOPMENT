import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
run = True

clock = pygame.time.Clock()
FPS = 60

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Ball:
   def __init__(self):
      self.size = randint(5,30)
      self.x = randint(0,WIDTH)
      self.y = randint(0,HEIGHT)
      self.generate_speed()
      self.generate_color()
   
   def generate_color(self):
      self.color = (randint(0,255),randint(0,255),randint(0,255))
   
   def generate_speed(self):
      self.x_change = randint(-3,3)
      self.y_change = randint(-2,2)
      while self.x_change == 0:
         self.x_change = randint(-3,3)
      while self.y_change == 0:
         self.y_change = randint(-2,2)
   
   def draw(self):
      pygame.draw.circle(screen,self.color,(self.x,self.y),self.size)

   def move(self):
      self.x += self.x_change 
      self.y += self.y_change
      if self.x < self.size or self.x > WIDTH - self.size:
         self.x_change *= -1
         self.generate_color()
      if self.y < self.size or self.y > HEIGHT - self.size:
         self.y_change *= -1  
         self.generate_color()

balls = [Ball(), Ball()]

while run:
   clock.tick(FPS)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            balls.append(Ball())
   
   for ball in balls:
      ball.move()

   screen.fill(black)
   for ball in balls:
      ball.draw()

   pygame.display.update()
   