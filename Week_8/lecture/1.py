import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
run = True
white = (255,255,255)
red = (255,0,0)

clock = pygame.time.Clock()
FPS = 60

surf = pygame.Surface((100,100))
surf.fill(red)
x,y = 10,10
dx,dy = 0, 0

while run:
   clock.tick(FPS)
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RIGHT:
            dx = 3
         if event.key == pygame.K_LEFT:
            dx = -3
         if event.key == pygame.K_UP:
            dy = -3
         if event.key == pygame.K_DOWN:
            dy = 3
   x += dx
   y += dy

   if x + 100 >= WIDTH or x < 0:
      dx *= -1
   if y + 100 >= HEIGHT or y < 0:
      dy *= -1
  
   screen.fill(white)

   screen.blit(surf,(x,y))

   pygame.display.update()

pygame.quit()


