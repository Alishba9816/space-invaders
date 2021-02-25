import random
import pygame
from pygame.locals import *
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("flappy birds")
gameExit = False
while not gameExit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameExit = True
  screen.fill(white)
  pygame.display.update()
pygame.quit()
