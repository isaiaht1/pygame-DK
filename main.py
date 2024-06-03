import pygame, sys
import time
from pygame.locals import QUIT
from pygame.locals import *


'''
def barrel_collision(cirlce_y, circle_x,radius,player_y, player_x)
  if abs(circle_y-(player_y+y_diffrence))+ abs(circle_x-(player_x+x_diffrence))<radius:
    Death()
def Death():
  global player_lives
  player_lives-=1
  Death_animation() #not making this right now
  if player_lives<=0:
    game_over()
  
    '''
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Donkey Kong')

kong = pygame.image.load("Donkey Kong.png")
kong = pygame.transform.scale(kong, (70, 70))

mario = pygame.image.load("luigi.png")
mario_right = pygame.transform.scale(mario, (40, 40))

mario_left = pygame.transform.flip(mario_right, True, False)
mario_run = mario_left

frame_counter=0
clock = pygame.time.Clock()

platform=False
ladder=False

bar_x = 100
bar_y = 70
mar_x = 320
mar_y = 220
jump_counter = 0
def draw_barrel(x, y):

  if frame_counter%45>22: 
    pygame.draw.circle(DISPLAYSURF, "brown", (x, y), 20)
    pygame.draw.line(DISPLAYSURF, "black", (x-10, y+10), (x+10, y-10))
    pygame.draw.line(DISPLAYSURF, "black", (x-10, y-10), (x+10, y+10))
  else:
    pygame.draw.circle(DISPLAYSURF, "brown", (x, y), 20)
    pygame.draw.line(DISPLAYSURF, "black", (x-10, y), (x+10, y))
    pygame.draw.line(DISPLAYSURF, "black", (x, y-10), (x, y+10))

  
while True:
    DISPLAYSURF.fill("cyan")
    #global bar_x, bar_y
    #add the time control
    clock.tick(45)
    # Draw the slanted platforms
    pygame.draw.line(DISPLAYSURF, "black", (10, 250), (375, 275), 8)
    pygame.draw.line(DISPLAYSURF, "green", (10, 195), (375, 170), 8)
    pygame.draw.line(DISPLAYSURF, "red", (10, 90), (375, 105), 8)

    # Draw the ladders
    pygame.draw.line(DISPLAYSURF, "brown", (40, 190), (40, 255), 24)
    pygame.draw.line(DISPLAYSURF, "yellow", (320, 95), (320, 180), 24)
  
    # The following lines will allow Mario to travel up the platforms and ladders. He can go both up and down.
    # Control the coordinates for the mario character
#top ladder
  
    if mar_x>=280 and mar_y<150 and mar_x<320 and mar_y>60:
      ladder=True
      #bottom ladder
    if mar_x >=10  and mar_x<50 and mar_y>145 and mar_y<230:
      ladder=True
#top platform
    if mar_y <=mar_x*15/365+65 and mar_y >=mar_x*15/365+45 and mar_x<365 and mar_x >=-15:
      if not ladder:
        mar_y = int(mar_x*15/365+50)
      platform=True
#middle platform
    if  mar_y< mar_x*15/365+170 and mar_x >=-15 and mar_x<365 and mar_y>mar_x*(-15)/365+140:
      if not ladder:  
        mar_y= int(mar_x*(-15)/365+147)
      platform=True
#bottom platform
    if mar_x >=-15 and mar_y>= mar_x*15/365+210 and mar_y<mar_x*15/365+250 and mar_x<365:
      if not ladder:
        mar_y = int(mar_x*15/365+215)
      platform=True
    
    #jump
    if platform and pygame.key.get_pressed()[K_SPACE]:
      mar_y -=30
      
      
    if platform or not ladder:
      if pygame.key.get_pressed()[K_LEFT]:
        mar_x += -2
        mario_run = mario_left
  
      if pygame.key.get_pressed()[K_RIGHT]:
        mar_x += 2
        mario_run = mario_right
    if ladder:
      if pygame.key.get_pressed()[K_UP]:
        mar_y -= 2
      if pygame.key.get_pressed()[K_DOWN]:
        mar_y += 2
    else:
      mar_y+=2

    ladder=False
    platform=False
      #would look smoother when going up if you added velocity solution, but you seemed hesitent about it in class, and it may or may not work well with jump, Id have to experiment. would look something like 
    
    '''if not disabled and pygame.key.get_pressed()[K_SPACE]:
        mar_y_velocity=-15
    elif disabled: 
         mar_y_velocity+=1
    else:
        mar_y_velocity=0
      #later down
        mar_y+=mar_y_velocity
       
    '''
    DISPLAYSURF.blit(kong, (0,20))
    DISPLAYSURF.blit(mario_run, (mar_x, mar_y))
  
    draw_barrel(bar_x, bar_y)
    if bar_x<325 and bar_y <=142:
      bar_x += 1 
      bar_y = int(bar_x*15/365+70) 
    elif bar_x>=325:
      bar_y+=1

    if bar_y > 142 and bar_y<185 and bar_x > 40:
      bar_x -= 1
      bar_y= int(bar_x*(-15)/365+167)

    elif bar_x <=40 and bar_y < 255:
      bar_y +=1

    if bar_x >=40 and bar_y>= 220:
      bar_x +=1
      bar_y = int(bar_x*15/365+230)

    frame_counter+=1
    
    for event in pygame.event.get():
      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()