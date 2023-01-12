import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
run = True

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)

clock = pygame.time.Clock()
FPS = 30

img = pygame.transform.scale(pygame.image.load('game_over.jpg'),(WIDTH,HEIGHT))

radius = 10
block = 5
body = [[radius,radius],[0,0],[0,0]]
dx,dy = block, 0

def own_round(value,base=5):
   return base * round(value/5)

def set_random_position():
   return own_round(random.randint(10,500)), own_round(random.randint(10,500))

food_x, food_y = set_random_position()

while run:
   clock.tick(FPS)
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RIGHT:
            dx = block
            dy = 0
         if event.key == pygame.K_LEFT:
            dx = -block
            dy = 0
         if event.key == pygame.K_DOWN:
            dx = 0
            dy = block
         if event.key == pygame.K_UP:
            dx = 0
            dy = -block
   
   for i in range(len(body)-1,0,-1):
      body[i][0] = body[i-1][0]
      body[i][1] = body[i-1][1]

   if abs(food_x - body[0][0]) <= radius and abs(food_y - body[0][1]) <= radius:
      food_x, food_y = set_random_position()
      FPS += 1
      body.append([body[0][0],body[0][1]])

   body[0][0] += dx
   body[0][1] += dy

   if body[0][0] >= 500:
      body[0][0] = 0
      screen.blit(img,(0,0))
      run = False

   if body[0][0] < 0:
      body[0][0] = 500
      screen.blit(img,(0,0))
      run = False

   if body[0][1] >= 500:
      body[0][1] = 0
      screen.blit(img,(0,0))
      run = False
   
   if body[0][1] < 0:
      body[0][1] = 500
      screen.blit(img,(0,0))
      run = False
   
   screen.fill(black)

   pygame.draw.circle(screen,blue,(food_x,food_y),radius)

   for i, (x,y) in enumerate(body):
      pygame.draw.circle(screen,red,(x,y),radius)
      
   pygame.display.update()

pygame.quit()