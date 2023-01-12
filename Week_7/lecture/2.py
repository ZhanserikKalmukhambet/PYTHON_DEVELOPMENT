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

while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            color = red if color == green else green
         if event.key == pygame.K_RIGHT:
            x = x + 10
         if event.key == pygame.K_LEFT:
            x = x - 10
         if event.key == pygame.K_UP:
            y = y - 10
         if event.key == pygame.K_DOWN:
            y = y + 10
      
   screen.fill(white)
      
   pygame.draw.rect(screen,color,(x,y,80,50))

   pygame.display.flip()
