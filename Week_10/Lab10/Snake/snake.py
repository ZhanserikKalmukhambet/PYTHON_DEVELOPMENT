import pygame, sys
from time import sleep
from random import randint
from pygame.math import Vector2
from _database import *

# start the game or not
username = input('Enter the username:\n')
mode = None
change = None

if does_exists(username):
   print('This account has already been registered!\nBelow your previous result:')
   show_previous_result(username)
   rq = input('Do you want to play again and update? "Yes" or "No" ?\n')
   if rq == 'Yes': 
      mode = 'Play'
      change = 'Update'
   else:
      print('Have a good day!')
else:
   mode = 'Play'
   change = 'Insert'
   

##########################################################

if mode == 'Play':

   pygame.init()

   # main parameters
   grid_size = 40
   grid_number = 20
   add = 400
   WIDTH, HEIGHT = grid_size*grid_number+add, grid_size*grid_number
   screen = pygame.display.set_mode((WIDTH,HEIGHT))
   pygame.display.set_caption('Snake Game')
   run = True
   font = pygame.font.SysFont('Cooper Black',grid_size)
   timer = 0

   # necessary colors
   bg_color = (175,215,70)
   grass_color = (167,209,61)
   snake_color = (255,0,0)

   # velocity of the snake
   clock = pygame.time.Clock()
   FPS = 10

   score = 0
   level = 0

   # types of food
   foods = [
            pygame.transform.scale(pygame.image.load('image/burger.png'),(40,40)),
            pygame.transform.scale(pygame.image.load('image/apple.png'),(40,40)),
            pygame.transform.scale(pygame.image.load('image/rabbit.png'),(40,40)),
            pygame.transform.scale(pygame.image.load('image/cola.png'),(40,40))
            ]

   # main function
   def draw_grass():
      for i in range(grid_number+add):
         if i % 2 == 0:
            for j in range(grid_number+add):
               if j % 2 == 0:
                  pygame.draw.rect(screen,grass_color,(i*grid_size,j*grid_size,grid_size,grid_size))
         else:
            for j in range(grid_number):
               if j % 2 != 0:
                  pygame.draw.rect(screen,grass_color,(i*grid_size,j*grid_size,grid_size,grid_size))

   def show_score(font):
      txt = font.render(f'Score {score}',True,(0,0,0))
      screen.blit(txt,(WIDTH-470,HEIGHT-40))

   def show_level(font):
      txt = font.render(f'Level {level}',True,(0,0,0))
      screen.blit(txt,(WIDTH-300,HEIGHT-40))

   def show_speed(font):
      txt = font.render(f'Speed {FPS}',True,(0,0,0))
      screen.blit(txt,(WIDTH-130,HEIGHT-40))


   #all info about wall
   class Wall:
      def __init__(self):
         self.body = []
         self.load_wall(level)
         self.draw()

      def load_wall(self,lvl):
         with open(f'levels/level{lvl}.txt', 'r') as f:
            wall_body = f.readlines()

         for i, line in enumerate(wall_body):
            for j, value in enumerate(line):
               if value == '#':
                  self.body.append([j*grid_size,i*grid_size])

      def draw(self):
         for x,y in self.body:
            pygame.draw.rect(screen,(255,255,0),(x,y,grid_size,grid_size))

   # all info about Food
   class Food:
      def __init__(self):
         i = randint(0,3)
         self.image = foods[i]
         self.cost = i + 1
         self.set_random_pos()

      def set_random_pos(self):
         self.x = randint(0,grid_number + (add/grid_size) - 1)
         self.y = randint(0,grid_number - 1)
         self.pos = Vector2(self.x, self.y)
         i = randint(0,3)
         self.image = foods[i]
         self.cost = i + 1

      def draw(self):
         food_rect = pygame.Rect(self.pos.x*grid_size, self.pos.y*grid_size, grid_size, grid_size)
         screen.blit(self.image, food_rect)

   # all info about snake
   class Snake:
      def __init__(self):
         self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
         self.dx = 1
         self.dy = 0
         self.right, self.left, self.up, self.down = True, False, False, False

      def draw(self):
         for cell in self.body:
            pygame.draw.rect(screen,snake_color,(cell.x*grid_size, cell.y*grid_size, grid_size, grid_size))

      def move(self):
         global timer
         for i in range(len(self.body)-1,0,-1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y =  self.body[i-1].y

         self.body[0].x += self.dx
         self.body[0].y += self.dy
         timer += 1
         if timer == 40:
            food.set_random_pos()
            timer = 0


      def check_fail(self):
      
         if self.body[0].x < 0 or self.body[0].x > grid_number+(add/grid_size)-1 or self.body[0].y < 0 or self.body[0].y > grid_number-1:
            # 1 case
            self.game_over()
         # 2 case
         for block in self.body[1:]:
            if block == self.body[0]:
               self.game_over()
         # 3 case
         for block in wall.body:
            if block == self.body[0]*grid_size:
               self.game_over()

      def game_over(self):
         # after game over send results to database
         if change == 'Insert':
            insert_data(username,level,score,FPS)
         else:
            update_data(level, score, FPS, username)

         # effects
         pygame.mixer.Sound('image/over.wav').play()
         sleep(3)
         pygame.quit()
         sys.exit()

   food = Food()
   snake = Snake()
   wall = Wall()

   screen_update = pygame.USEREVENT
   pygame.time.set_timer(screen_update,150)

   while run:
      clock.tick(FPS)

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
            sys.exit()
         if event.type == screen_update:
            snake.move()
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               if snake.dx != -1:
                  snake.dx = 1
                  snake.dy = 0
            if event.key == pygame.K_LEFT:
               if snake.dx != 1:
                  snake.dx = -1
                  snake.dy = 0
            if event.key == pygame.K_DOWN:
               if snake.dy != -1:
                  snake.dx = 0
                  snake.dy = 1
            if event.key == pygame.K_UP:
               if snake.dy != 1:
                  snake.dx = 0
                  snake.dy = -1
            if event.key == pygame.K_SPACE:
               sleep(2)

      # main patterns of the game
      screen.fill(bg_color)
      draw_grass()
      show_score(font)
      show_level(font)
      show_speed(font)

      # drawing the food randomly
      food.draw()

      # drawing the snake body
      snake.draw()

      # drawing load
      wall.draw()

      # check wether the snake-head collides with border or eats itself
      snake.check_fail()

      # check the collision == > eating the food
      if snake.body[0] == food.pos:
         # Randomly generating food with different weights
         score += food.cost
         FPS += 1
         if score>level*10:
            level+=1
            wall.load_wall(0)
            wall.load_wall(level)

         # Foods which are disappearing after some time(timer)
         timer = 0

         snake.body.append(Vector2(snake.body[len(snake.body)-1].x, snake.body[len(snake.body)-1].y))
         food.set_random_pos()

         # sound of eating food
         pygame.mixer.Sound('image/snake_eat.wav').play()

         # check again whether the food is appearing on the snake's body
         for block in snake.body[1:]:
            while block == food.pos:
               food.set_random_pos()


      pygame.display.update()

   pygame.quit()
