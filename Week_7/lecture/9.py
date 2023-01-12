import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
running = True
# color = RGB ==> [0,255]
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

color = BLUE

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('musics/music.mp3')
pygame.mixer.music.play()

while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            color = GREEN if color == BLUE else BLUE
      if event.type == SONG_END:
         print('The song is ended!')
   
   pygame.draw.rect(screen, color, (100,100,200,100))
   # pygame.draw.circle(screen,green,(50,50),50)

   pygame.display.flip()
