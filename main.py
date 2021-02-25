import random
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("flappy birds")
gameExit = False
while not gameExit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameExit = True

pygame.quit()


