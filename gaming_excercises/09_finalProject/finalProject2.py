# Final Project, Alexandra Sculley, v0.9

import pygame, sys, random 
from sys import exit
clock = pygame.time.Clock()
x = 1318
y = 1080
xSlotOp1, xSlotOp2, xSlotOp3 = 1020, 860, 700
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
gameScreen = pygame.image.load('img/DungeonRoom.png')

# Player
playerSurf = pygame.image.load('img/slot.png')
playerX, playerY = 900, 200

# Rectangles
gameRect = gameScreen.get_rect(bottomleft = (gameScreenX, gameScreenY))

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
    #print(playerX)
    #print(playerY)

    screen.blit(slot1.Image, (slot1.xValue, slot1.yValue))
    screen.blit(slot2.Image, (slot2.xValue, slot2.yValue))
    screen.blit(slot3.Image, (slot3.xValue, slot3.yValue))
    screen.blit(slot4.Image, (slot4.xValue, slot4.yValue))
    screen.blit(slot5.Image, (slot5.xValue, slot5.yValue))
    screen.blit(slot6.Image, (slot6.xValue, slot6.yValue))
    screen.blit(gameScreen, gameRect)
    screen.blit(playerSurf, (playerX, playerY))
    #window.fill((0, 0, 0))
    pygame.display.update()