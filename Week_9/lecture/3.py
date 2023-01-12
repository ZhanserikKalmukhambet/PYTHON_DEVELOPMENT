import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
run = True

clock = pygame.time.Clock()
FPS = 7

black = (0,0,0)
white = (255,255,255)
red = (155,0,0)
green = (0,155,0)
blue = (0,0,155)

# grid
block_size = 20
grid_color = (100,100,100)

# score
cnt = 0

def draw_grid():
   for x in range(0,WIDTH,block_size):
      for y in range(0,HEIGHT,block_size):
         pygame.draw.rect(screen,grid_color,(x,y,block_size,block_size),1)

# snake
class Snake:
   def __init__(self):
      self.body = [[11,10],[10,10]]
      self.block = 1
      self.dx = self.block
      self.dy = 0
   
   def draw(self):
      for i,(x,y) in enumerate(self.body):
         color = red if i==0 else green
         pygame.draw.rect(screen,color,(x*block_size,y*block_size,20,20))
   
   def move(self):
      for i in range(len(self.body)-1,0,-1):
         self.body[i][0] = self.body[i-1][0]
         self.body[i][1] = self.body[i-1][1]
      
      self.body[0][0] += self.dx
      self.body[0][1] += self.dy

# wall
lvl = 1

class Wall:
   def __init__(self):
      self.body = []
      self.load_wall(lvl)
   
   def load_wall(self,lvl):
      with open(f'level{lvl}.txt', 'r') as f:
         wall_body = f.readlines()

      for i, line in enumerate(wall_body):
         for j, value in enumerate(line):
            if value == '#':
               self.body.append([j*block_size,i*block_size])

   def draw(self):
      for x,y in self.body:
         pygame.draw.rect(screen,(255,0,0),(x,y,block_size,block_size))

# food
class Food:
   def __init__(self):
      self.generate_random_pos()
   
   def generate_random_pos(self):
      self.x = self.my_round(randint(0,WIDTH-block_size))
      self.y = self.my_round(randint(0,HEIGHT-block_size))
   
   def my_round(self, value, base=block_size):
      return base * round(value / base)
   
   def draw(self):
      pygame.draw.rect(screen, blue, (self.x, self.y, block_size, block_size))

snake = Snake()
food = Food()
wall = Wall()

while run:
   clock.tick(FPS)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RIGHT:
            snake.dx = snake.block
            snake.dy = 0
         if event.key == pygame.K_LEFT:
            snake.dx = -snake.block
            snake.dy = 0
         if event.key == pygame.K_UP:
            snake.dx = 0
            snake.dy = -snake.block
         if event.key == pygame.K_DOWN:
            snake.dx = 0
            snake.dy = snake.block
           
   screen.fill(black)
   draw_grid()

   font = pygame.font.SysFont('Calibri',30)
   score = font.render(f'Score: {cnt}',True,(255,0,0))
   screen.blit(score,(20,20))

   snake.draw()
   snake.move()

   food.draw()

   wall.draw()

   if snake.body[0][0]*block_size == food.x and snake.body[0][1]*block_size == food.y:
      snake.body.append([snake.body[0][0],snake.body[0][1]])
      food.generate_random_pos()
      cnt += 1
      if cnt % 5 == 0:
         lvl += 1
         wall.load_wall(lvl)

   pygame.display.update()