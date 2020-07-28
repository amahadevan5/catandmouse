import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake and Mouse')

clock = pygame.time.Clock()

snake1_block = 10
snake1_speed = 80

font_style = pygame.font.SysFont(None, 30)


def message(msg, color):
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [dis_width / 3, dis_height / 3])


def gameLoop():  # creating a function
  game_over = False
  game_close = False

  x1 = dis_width / 2
  y1 = dis_height / 2

  # num pixels mouse moves per refresh when respective key is clicked
  speed_mouse_x = 8
  speed_mouse_y = 8

  #this is like x1_change/x2_change but for the mouse
  mouse_change_x = 0
  mouse_change_y = 0

  x1_change = 0
  y1_change = 0


  mousex = round(random.randrange(0, dis_width - snake1_block) / 10.0) * 10.0
  mousey = round(random.randrange(0, dis_width - snake1_block) / 10.0) * 10.0

  while not game_over:

     while game_close == True:
        dis.fill(white)
        message("You Lost! Press Q-Quit or C-Play Again", red)
        pygame.display.update()

        for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_q:
                 game_over = True
                 game_close = False
              if event.key == pygame.K_c:
                 gameLoop()

     for event in pygame.event.get():
         #keys for the snake
        if event.type == pygame.QUIT:
           game_over = True
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
              x1_change = -snake1_block
              y1_change = 0
           elif event.key == pygame.K_RIGHT:
              x1_change = snake1_block
              y1_change = 0
           elif event.key == pygame.K_UP:
              y1_change = -snake1_block
              x1_change = 0
           elif event.key == pygame.K_DOWN:
              y1_change = snake1_block
              x1_change = 0
           #keys for the mouse
           if event.key == pygame.K_w:
              mouse_change_x = 0
              mouse_change_y = -speed_mouse_y
           elif event.key == pygame.K_s:
              mouse_change_x = 0
              mouse_change_y = speed_mouse_y
           elif event.key == pygame.K_a:
              mouse_change_x = -speed_mouse_x
              mouse_change_y = 0
           elif event.key == pygame.K_d:
              mouse_change_x = speed_mouse_x
              mouse_change_y = 0


     if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_close = True

     if (x1 == mousex + snake1_block or x1 == mousex - snake1_block) and (y1 == mousey + snake1_block or y1 == mousey - snake1_block):
        game_close = True

     #this stuff makes the mouse bounce
     if mousex > dis_width or mousex < 0:
        mouse_change_x *= -1
     if mousey > dis_height or mousey < 0:
        mouse_change_y *= -1

     x1 += x1_change
     y1 += y1_change
     mousex += mouse_change_x
     mousey += mouse_change_y
     dis.fill(white)
     pygame.draw.rect(dis, blue, [mousex, mousey, snake1_block, snake1_block])
     pygame.draw.rect(dis, black, [x1, y1, snake1_block, snake1_block])
     pygame.display.update()

     if x1 == mousex and y1 == mousey:
        game_close = True
     clock.tick(snake1_speed)

  pygame.quit()
  quit()


gameLoop()



