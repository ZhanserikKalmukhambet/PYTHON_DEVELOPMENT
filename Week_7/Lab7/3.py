import pygame
import os

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Red Ball')
running = True

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

clock = pygame.time.Clock()
FPS = 60

r = 25
x,y = 25, 25
vel = 20


while running: 

   clock.tick(FPS)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      
   pressed = pygame.key.get_pressed()
   
   if pressed[pygame.K_RIGHT] and x < WIDTH - r - vel:
      x += vel
   if pressed[pygame.K_LEFT] and x >= r + 5:
      x -= vel
   if pressed[pygame.K_UP] and y >= r + 5:
      y -= vel
   if pressed[pygame.K_DOWN] and y < HEIGHT - r - vel:
      y += vel
   
   screen.fill(white)

   pygame.draw.circle(screen,red,(x,y),r)

   pygame.display.update()

pygame.quit()
   