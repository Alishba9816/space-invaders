import random
import pygame
from pygame.locals import *
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
GAME_SPRITES={}
icon=pygame.image.load('lo.png')
bgimg= pygame.image.load('giimg.jpg')
screen = pygame.display.set_mode((450,400))
pygame.display.set_caption("flappy birds")
pygame.display.set_icon(icon)
gameExit = False
while not gameExit:
  screen.fill(white)
  screen.blit(bgimg, (0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameExit = True
  pygame.display.update()
pygame.quit()
