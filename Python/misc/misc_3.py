import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Basic shapes")

yellow = (255, 255, 0)

black = (0, 0, 0)

blue = (0, 0, 255)

while True:
    screen.fill(yellow)
    pygame.draw.rect(screen, black, (300, 300, 200, 100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()