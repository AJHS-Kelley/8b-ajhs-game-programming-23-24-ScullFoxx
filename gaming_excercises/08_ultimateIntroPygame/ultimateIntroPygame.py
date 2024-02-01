# ultimateIntroPygame Sculley, Alexandra, v0.1

import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()


testSurface = pygame.Surface((100,200))
testSurface.fill('Red')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    # update everything
    screen.blit(testSurface, (0,0))
    pygame.display.update()
    clock.tick(60)
