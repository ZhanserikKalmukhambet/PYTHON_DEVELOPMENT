import pygame as pg
import random

pg.init()

screen = pg.display.set_mode((500,500))
running = True

# screen.fill((0,128,255))

green = (0,255,0)
red = (255,0,0)
white = (255,255,255)

color = green

x,y = 10, 10

clock = pg.time.Clock()
FPS = 60

img = pg.image.load('img1.png')

song_end = pg.USEREVENT + 1
pg.mixer.music.set_endevent(song_end)
pg.mixer.music.load('music.mp3')
pg.mixer.music.play()

while running:
   for event in pg.event.get():
      if event.type == pg.QUIT:
         running = False
      if event.type == song_end:
         print('The song ended !')
      
   pressed = pg.key.get_pressed()

   if pressed[pg.K_UP]:
      y = y - 3
   if pressed[pg.K_DOWN]:
      y = y + 3
   if pressed[pg.K_RIGHT]:
      x = x + 3
   if pressed[pg.K_LEFT]:
      x = x - 3

   if x >= 500:
      x = 0
   if y >= 500:
      y = 0
      
   screen.fill(white)
      
   screen.blit(img,(x,y))

   pg.display.flip()

   clock.tick(FPS)