# Final Project, Alexandra Sculley, v0.0

import pygame, sys, random 
from sys import exit
clock = pygame.time.Clock()
resolution = 0 # 0 = Low resolution (800, 600), 1 = high resolution (1920, 1080)
if resolution == 0:
    x = 800
    y = 600
    xButOp1 = 200
    yButOp1 = 400
    xButOp2 = 100
    yButOp2 = 1
    xButOp3 = 1
    xSlotOp1 = 1
    xSlotOp2 = 1
    xSlotOp3 = 1
elif resolution == 1:
    x = 1920
    y = 1080
    xButOp1 = 260
    yButOp1 = 830
    xButOp2 = 100
    yButOp2 = 990
    xButOp3 = 420
    xSlotOp1 = 1800
    xSlotOp2 = 1640
    xSlotOp3 = 1480

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
buttonUPSurf = pygame.image.load('img/buttonUp.png')
buttonUPRect = buttonUPSurf.get_rect(center = (xButOp1, yButOp1))
buttonDOWNSurf = pygame.image.load('img/buttonDown.png')
buttonDOWNRect = buttonDOWNSurf.get_rect(center = (xButOp1, yButOp2))
buttonLEFTSurf = pygame.image.load('img/buttonLeft.png')
buttonLEFTRect = buttonLEFTSurf.get_rect(center = (xButOp2, yButOp2))
buttonRIGHTSurf = pygame.image.load('img/buttonRight.png')
buttonRIGHTRect = buttonRIGHTSurf.get_rect(center = (xButOp3, yButOp2))
slot1Surf = pygame.image.load('img/slot.png')
slot1Rect = slot1Surf.get_rect(center = (xSlotOp1, yButOp2))
slot2Surf = pygame.image.load('img/slot.png')
slot2Rect = slot2Surf.get_rect(center = (xSlotOp1, yButOp1))
slot3Surf = pygame.image.load('img/slot.png')
slot3Rect = slot3Surf.get_rect(center = (xSlotOp2, yButOp1))
slot4Surf = pygame.image.load('img/slot.png')
slot4Rect = slot4Surf.get_rect(center = (xSlotOp2, yButOp2))
slot5Surf = pygame.image.load('img/slot.png')
slot5Rect = slot5Surf.get_rect(center = (xSlotOp3, yButOp2))
slot6Surf = pygame.image.load('img/slot.png')
slot6Rect = slot5Surf.get_rect(center = (xSlotOp3, yButOp1))
#rulerSurf = pygame.image.load('img/stick.png')
#rulerRect = rulerSurf.get_rect(topleft = (0, 720))
gameScreen = pygame.image.load('img/DungeonRoom.png')
gameRect = gameScreen.get_rect(bottomleft = (600,730))
playerSurf = pygame.image.load('img/slot.png')
playerRect = playerSurf.get_rect(center = (900, 200))

if resolution == 0:
    gameScreen = pygame.transform.rotozoom(gameScreen, 1, 0.5)
    buttonUPSurf = pygame.transform.rotozoom(buttonUPSurf, 1, 0.7)
    buttonDOWNSurf = pygame.transform.rotozoom(buttonDOWNSurf, 1, 0.7)
    buttonLEFTSurf = pygame.transform.rotozoom(buttonLEFTSurf, 1, 0.7)
    buttonRIGHTSurf = pygame.transform.rotozoom(buttonRIGHTSurf, 1, 0.7)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonUPRect.collidepoint(event.pos):
                playerRect.y -= 10
            if buttonDOWNRect.collidepoint(event.pos):
                playerRect.y += 50
            if buttonLEFTRect.collidepoint(event.pos):
                playerRect.x -= 50
            if buttonRIGHTRect.collidepoint(event.pos):
                playerRect.x += 50

    #screen.blit(barSurf, barRect)
    screen.blit(buttonUPSurf, buttonUPRect)
    screen.blit(buttonDOWNSurf, buttonDOWNRect)
    screen.blit(buttonLEFTSurf, buttonLEFTRect)
    screen.blit(buttonRIGHTSurf, buttonRIGHTRect)
    screen.blit(slot1Surf, slot1Rect)
    screen.blit(slot2Surf, slot2Rect)
    screen.blit(slot3Surf, slot3Rect)
    screen.blit(slot4Surf, slot4Rect)
    screen.blit(slot5Surf, slot5Rect)
    screen.blit(slot6Surf, slot6Rect)
 #   screen.blit(rulerSurf, rulerRect)
    screen.blit(gameScreen, gameRect)
    screen.blit(playerSurf, playerRect)










    pygame.display.update()
    clock.tick(60)
