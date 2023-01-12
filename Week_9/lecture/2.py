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

class Ball(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.x = randint(0,WIDTH)
      self.y = randint(0,HEIGHT)
      self.image = pygame.Surface([20,20])
      self.rect = self.image.get_rect(center=(self.x,self.y))
      self.generate_speed()
      self.generate_color()
      self.image.fill(self.color)
   
   def generate_color(self):
      self.color = (randint(0,255),randint(0,255),randint(0,255))
   
   def generate_speed(self):
      self.x_change = randint(-3,3)
      self.y_change = randint(-2,2)
      while self.x_change == 0:
         self.x_change = randint(-3,3)
      while self.y_change == 0:
         self.y_change = randint(-2,2)
   
   def update(self):
      self.rect.x += self.x_change 
      self.rect.y += self.y_change
      if self.rect.x < 0 or self.rect.x > WIDTH - 20:
         self.x_change *= -1
         self.generate_color()
      if self.rect.y < 0 or self.rect.y > HEIGHT - 20:
         self.y_change *= -1  
         self.generate_color()

balls = pygame.sprite.Group()
balls.add(Ball())

while run:
   clock.tick(FPS)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            balls.add(Ball())

   screen.fill(black)
   
   balls.draw(screen)
   
   balls.update()

   pygame.display.update()