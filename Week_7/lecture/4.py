import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
running = True

blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

color = green

x,y = 10, 10

width, height = 80, 50

clock = pygame.time.Clock()
FPS = 60

img = pygame.image.load('img1.png')

while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      
   pressed = pygame.key.get_pressed()

   if pressed[pygame.K_UP]:
      y = y - 3
   if pressed[pygame.K_DOWN]:
      y = y + 3
   if pressed[pygame.K_RIGHT]:
      x = x + 3
   if pressed[pygame.K_LEFT]:
      x = x - 3

   if x >= 500:
      x = 0
   if y >= 500:
      y = 0
      
   screen.fill(white)
      
   screen.blit(img,(x,y))
   # pygame.draw.rect(screen,color,(x,y,width,height))

   pygame.display.flip()

   clock.tick(FPS)