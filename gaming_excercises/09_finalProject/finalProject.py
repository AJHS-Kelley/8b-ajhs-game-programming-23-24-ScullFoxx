# Final Project, Alexandra Sculley, v0.0

import pygame, sys, random 
from sys import exit
clock = pygame.time.Clock()

resolution = 1 # 0 = Low resolution (800, 600), 1 = high resolution (1920, 1080)
if resolution == 0:
    x = 800
    y = 600
elif resolution == 1:
    x = 1920
    y = 1080

screen = pygame.display.set_mode((x, y))

#while True:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()
#            exit()

# pygame.init()

# difficulty = int(input("Please select a difficulty. Enter 1 for Short Dungeon and 2 for Long Dungeon\n"))

# if difficulty == 1:
#     z = "Dungeon Explorer: Short dungeon"
# else:
#     z = "Dungeon Explorer: Long dungeon"

# pygame.display.set_caption(z)

barSurf = pygame.image.load('img/bar.png')
barRect = barSurf.get_rect(topleft = (0,730))
button1Surf = pygame.image.load('img/button.png')
button1Rect = button1Surf.get_rect(center = (260, 830))
button2Surf = pygame.image.load('img/button.png')
button2Rect = button2Surf.get_rect(center = (260, 990))
button3Surf = pygame.image.load('img/button.png')
button3Rect = button3Surf.get_rect(center = (100, 990))
button4Surf = pygame.image.load('img/button.png')
button4Rect = button4Surf.get_rect(center = (420, 990))
slot1Surf = pygame.image.load('img/slot.png')
slot1Rect = slot1Surf.get_rect(center = (1800, 990))
slot2Surf = pygame.image.load('img/slot.png')
slot2Rect = slot2Surf.get_rect(center = (1800, 830))
slot3Surf = pygame.image.load('img/slot.png')
slot3Rect = slot3Surf.get_rect(center = (1640, 830))
slot4Surf = pygame.image.load('img/slot.png')
slot4Rect = slot4Surf.get_rect(center = (1640, 990))
slot5Surf = pygame.image.load('img/slot.png')
slot5Rect = slot5Surf.get_rect(center = (1480, 990))
slot6Surf = pygame.image.load('img/slot.png')
slot6Rect = slot5Surf.get_rect(center = (1480, 830))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #screen.blit(barSurf, barRect)
    screen.blit(button1Surf, button1Rect)
    screen.blit(button2Surf, button2Rect)
    screen.blit(button3Surf, button3Rect)
    screen.blit(button4Surf, button4Rect)
    screen.blit(slot1Surf, slot1Rect)
    screen.blit(slot2Surf, slot2Rect)
    screen.blit(slot3Surf, slot3Rect)
    screen.blit(slot4Surf, slot4Rect)
    screen.blit(slot5Surf, slot5Rect)
    screen.blit(slot6Surf, slot6Rect)
    










    pygame.display.update()
    clock.tick(60)
