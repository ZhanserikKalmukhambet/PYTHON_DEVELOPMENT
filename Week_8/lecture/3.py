import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
color = white # bt default

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

game_over = False

prev, cur = None, None
screen.fill(black)

width_line = 1

while not game_over:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game_over = True
      
      # drawing 
      if event.type == pygame.MOUSEBUTTONDOWN:
         prev = pygame.mouse.get_pos()
      if event.type == pygame.MOUSEMOTION:
         cur = pygame.mouse.get_pos()
         if prev:
            pygame.draw.line(screen,color,prev,cur,width_line)
            prev = cur
      if event.type == pygame.MOUSEBUTTONUP:
         prev = None
      
      # close the window
      pressed = pygame.key.get_pressed()

      alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
      ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            screen.fill(black)
         if event.key == pygame.K_F4 and alt_held:
            run = False
         if event.key == pygame.K_w and ctrl_held:
            run = False
         if event.key == pygame.K_ESCAPE:
            run = False
         if event.key == pygame.K_UP:
            width_line += 1
         if event.key == pygame.K_DOWN:
            width_line -= 1
         if event.key == pygame.K_r:
            color = red
         if event.key == pygame.K_g:
            color = green
         if event.key == pygame.K_b:
            color = blue

   pygame.display.update()
   clock.tick(30)
