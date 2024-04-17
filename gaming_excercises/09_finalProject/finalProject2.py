# Final Project, Alexandra Sculley, v0.9

import pygame, sys, random 
from sys import exit
clock = pygame.time.Clock()
x = 1920
y = 1080
xButOp1, xButOp2, xButOp3 = 260, 100, 420
yButOp1, yButOp2 = 830, 990
xSlotOp1, xSlotOp2, xSlotOp3 = 1760, 1600, 1440
gameScreenX, gameScreenY = 600, 730
leftCeiling, rightCeiling, floorCeiling, topCeiling =  700, 1060, 478, 78

screen = pygame.display.set_mode((x, y))

class InventorySlots: # Use PascalCase for ClassNames
    def __init__(self, xValue, yValue): 
        self.xValue = xValue
        self.yValue = yValue
        self.Image = pygame.image.load('Img/slot.png')
        self.Scale = None

# Surfaces
slot1 = InventorySlots(xSlotOp1, 760)
slot2 = InventorySlots(xSlotOp1, 920)
slot3 = InventorySlots(xSlotOp2, 920)
slot4 = InventorySlots(xSlotOp2, 760)
slot5 = InventorySlots(xSlotOp3, 760)
slot6 = InventorySlots(xSlotOp3, 920)
buttonUPSurf = pygame.image.load('img/buttonUp.png')
buttonDOWNSurf = pygame.image.load('img/buttonDown.png')
buttonLEFTSurf = pygame.image.load('img/buttonLeft.png')
buttonRIGHTSurf = pygame.image.load('img/buttonRight.png')
gameScreen = pygame.image.load('img/DungeonRoom.png')

# Player
playerSurf = pygame.image.load('img/slot.png')
playerX, playerY = 900, 200

# Rectangles
gameRect = gameScreen.get_rect(bottomleft = (gameScreenX, gameScreenY))
buttonUPRect = buttonUPSurf.get_rect(center = (xButOp1, yButOp1))
buttonDOWNRect = buttonDOWNSurf.get_rect(center = (xButOp1, yButOp2))
buttonLEFTRect = buttonLEFTSurf.get_rect(center = (xButOp2, yButOp2))
buttonRIGHTRect = buttonRIGHTSurf.get_rect(center = (xButOp3, yButOp2))

vel = 3
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if playerY > topCeiling:
            playerY -= vel
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if playerX < rightCeiling:
            playerX += vel
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if playerY < floorCeiling:
            playerY += vel
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if playerX > leftCeiling:
            playerX -= vel

    screen.blit(slot1.Image, (slot1.xValue, slot1.yValue))
    screen.blit(slot2.Image, (slot2.xValue, slot2.yValue))
    screen.blit(slot3.Image, (slot3.xValue, slot3.yValue))
    screen.blit(slot4.Image, (slot4.xValue, slot4.yValue))
    screen.blit(slot5.Image, (slot5.xValue, slot5.yValue))
    screen.blit(slot6.Image, (slot6.xValue, slot6.yValue))
    screen.blit(buttonRIGHTSurf, buttonRIGHTRect)
    screen.blit(buttonUPSurf, buttonUPRect)
    screen.blit(buttonLEFTSurf, buttonLEFTRect)
    screen.blit(buttonDOWNSurf, buttonDOWNRect)
    screen.blit(gameScreen, gameRect)
    screen.blit(playerSurf, (playerX, playerY))
    #window.fill((0, 0, 0))
    pygame.display.update()