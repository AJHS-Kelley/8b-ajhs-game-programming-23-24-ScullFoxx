# Final Project, Alexandra Sculley, v0.9

import pygame, sys, random 
from sys import exit
clock = pygame.time.Clock()

def clockyCounty():
    currentTimer = int(pygame.time.get_ticks() / 1000)
resolution = 0 # 0 = Low resolution (800, 600), 1 = high resolution (1920, 1080)
if resolution == 0:
    x = 800
    y = 600
    xButOp1 = 180
    yButOp1 = 430
    xButOp2 = 70
    yButOp2 = 540
    xButOp3 = 290
    xSlotOp1 = 740
    xSlotOp2 = 628
    xSlotOp3 = 516
    gameScreenX = 200
    gameScreenY = 370
    playerX = 300
    playerY = 300
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
    gameScreenX = 600
    gameScreenY = 730
    playerX = 900
    playerY = 200

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
buttonDOWNSurf = pygame.image.load('img/buttonDown.png')
buttonLEFTSurf = pygame.image.load('img/buttonLeft.png')
buttonRIGHTSurf = pygame.image.load('img/buttonRight.png')
slot1Surf = pygame.image.load('img/slot.png')
slot2Surf = pygame.image.load('img/slot.png')
slot3Surf = pygame.image.load('img/slot.png')
slot4Surf = pygame.image.load('img/slot.png')
slot5Surf = pygame.image.load('img/slot.png')
slot6Surf = pygame.image.load('img/slot.png')
#rulerSurf = pygame.image.load('img/stick.png')
#rulerRect = rulerSurf.get_rect(topleft = (0, 720))
gameScreen = pygame.image.load('img/DungeonRoom.png')
playerSurf = pygame.image.load('img/slot.png')

if resolution == 0:
    gameScreen = pygame.transform.rotozoom(gameScreen, 0.3, 0.5)
    buttonUPSurf = pygame.transform.rotozoom(buttonUPSurf, 0.3, 0.7)
    buttonDOWNSurf = pygame.transform.rotozoom(buttonDOWNSurf, 0.3, 0.7)
    buttonLEFTSurf = pygame.transform.rotozoom(buttonLEFTSurf, 0.3, 0.7)
    buttonRIGHTSurf = pygame.transform.rotozoom(buttonRIGHTSurf, 0.3, 0.7)
    slot1Surf = pygame.transform.rotozoom(slot1Surf, 0.3, 0.7)
    slot2Surf = pygame.transform.rotozoom(slot2Surf, 0.3, 0.7)
    slot3Surf = pygame.transform.rotozoom(slot3Surf, 0.3, 0.7)
    slot4Surf = pygame.transform.rotozoom(slot4Surf, 0.3, 0.7)
    slot5Surf = pygame.transform.rotozoom(slot5Surf, 0.3, 0.7)
    slot6Surf = pygame.transform.rotozoom(slot6Surf, 0.3, 0.7)
    playerSurf = pygame.transform.rotozoom(playerSurf, 0.000001, 0.4)

playerRect = playerSurf.get_rect(center = (playerX, playerY))
gameRect = gameScreen.get_rect(bottomleft = (gameScreenX, gameScreenY))
buttonUPRect = buttonUPSurf.get_rect(center = (xButOp1, yButOp1))
buttonDOWNRect = buttonDOWNSurf.get_rect(center = (xButOp1, yButOp2))
buttonLEFTRect = buttonLEFTSurf.get_rect(center = (xButOp2, yButOp2))
buttonRIGHTRect = buttonRIGHTSurf.get_rect(center = (xButOp3, yButOp2))
slot1Rect = slot1Surf.get_rect(center = (xSlotOp1, yButOp2))
slot2Rect = slot2Surf.get_rect(center = (xSlotOp1, yButOp1))
slot3Rect = slot3Surf.get_rect(center = (xSlotOp2, yButOp1))
slot4Rect = slot4Surf.get_rect(center = (xSlotOp2, yButOp2))
slot5Rect = slot5Surf.get_rect(center = (xSlotOp3, yButOp2))
slot6Rect = slot5Surf.get_rect(center = (xSlotOp3, yButOp1))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonUPRect.collidepoint(event.pos):
                while playerRect.y > 42:
                    playerRect.y -= 1
            if buttonDOWNRect.collidepoint(event.pos):
                while playerRect.y < 259:
                    playerRect.y += 1
            if buttonLEFTRect.collidepoint(event.pos):
                while playerRect.x > 250:
                    playerRect.x -= 1
            if buttonRIGHTRect.collidepoint(event.pos):
                while playerRect.x < 445:
                    playerRect.x += 1

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
