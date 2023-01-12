import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

size = (500,400)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption('PyGame example') # name of the file
running = True

while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
   
   screen.fill(white) # all shapes should be drown after the filling background

   pygame.draw.line(screen,red,[50,50],[400,50],5)
   for i in range(10,100,10):
      pygame.draw.line(screen,green,[50,50+i],[400,50+i],3)

   # text
   font = pygame.font.Font(None,50) # height of the text
   text1 = font.render('My text #1',True,red)
   text2 = font.render('My text #2',False,red)
   screen.blit(text1,(0,300))
   screen.blit(text2,(0,350))

   pygame.draw.polygon(screen,green,[(100,100),(45,90),(200,350),(20,400)],2)

   pygame.display.flip()

pygame.quit()


