import pygame
import os

pygame.init()

WIDTH, HEIGHT = 1000, 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('MUSIC Player')
clock = pygame.time.Clock()
FPS = 60
running = True

white = (255,255,255)
black = (0,0,0)
gray = (127,127,127)
red = (255,0,0)
blue = (0,0,255)

color = blue
color_next, color_previous = white, white

bg_image = pygame.transform.scale(pygame.image.load(os.path.join('images','music_1.png')),(WIDTH,HEIGHT))
img1 = pygame.transform.scale(pygame.image.load(os.path.join('images','music_2.png')),(200,200))
img2 = pygame.transform.scale(pygame.image.load(os.path.join('images','music_3.png')),(600,350))

font = pygame.font.Font(None,150) # height of the text
text = font.render('Tracks',True,white)

start_x, start_y = 250, 600

end_x, end_y = 750, 600

R = 40 # radius of play\stop button

def show_screen():

   screen.fill(black)
   
   screen.blit(bg_image,(0,0))
   screen.blit(img1,(0,0))
   screen.blit(img1,(800,0))
   screen.blit(img2,(200,200))
   screen.blit(text,(WIDTH/2 - int(text.get_width()/2),50))

   pygame.draw.line(screen,white, (start_x,start_y), (end_x,end_y), 7)
   pygame.draw.circle(screen, red, (start_x,start_y), 10)

   pygame.draw.circle(screen,white,(WIDTH/2, 700), R,5)
   
   pygame.draw.polygon(screen,color,[(WIDTH/2-15,700-15),(WIDTH/2+15,700-15),(WIDTH/2-15,700+15),(WIDTH/2+15,700+15)])

   pygame.draw.polygon(screen,color_next,[(WIDTH/2+100,700 - R),(WIDTH/2+100+40,700+35 - R),(WIDTH/2+100,700+70 - R)])
   pygame.draw.polygon(screen,color_previous,[(WIDTH/2-100,700 - R),(WIDTH/2-100-40,700+35 - R),(WIDTH/2-100,700+70 - R)])

   pygame.display.update()


songs = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3', 'song_4.mp3', 'song_5.mp3']

def play_next_song(color):
   global songs
   songs = songs[1:] + [songs[0]]
   current = songs[0]
   if color == red:
      pygame.mixer.music.load(current)
      pygame.mixer.music.play()
   return current

current = play_next_song(color)

def check(color):
   global current
   if color == red:
      pygame.mixer.music.load(current)
      pygame.mixer.music.play()
   else:
      pygame.mixer.music.stop() 

while running:

   clock.tick(60)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False

      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            color = red if color == blue else blue
            check(color)
            
         if event.key == pygame.K_RIGHT:
            play_next_song(color)
      
   show_screen()

pygame.quit()