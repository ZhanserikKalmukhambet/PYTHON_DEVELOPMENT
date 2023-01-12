import pygame, os

pygame.init()

screen = pygame.display.set_mode((500,500))
running = True
# color = RGB ==> [0,255]
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

color = BLUE

font = pygame.font.SysFont('Calibri',30)
txt = font.render('Hello, World!', True, (0,0,0))

songs = [os.path.join('musics','ayree2.mp3'), os.path.join('musics','ayree1.mp3'), os.path.join('musics','ayree3.mp3')]

# playing in the sequence
def play_next_song():
   global songs
   songs = songs[1:] + [songs[0]] # move the current to the end
   pygame.mixer.music.load(songs[0])
   pygame.mixer.music.play()

while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            color = GREEN if color == BLUE else BLUE
   
   screen.fill((255,255,255))

   pygame.draw.rect(screen, color, (100,100,200,100))
   
   screen.blit(txt,(250-txt.get_width()/2, 250-txt.get_height()/2))

   play_next_song()

   pygame.display.flip()
