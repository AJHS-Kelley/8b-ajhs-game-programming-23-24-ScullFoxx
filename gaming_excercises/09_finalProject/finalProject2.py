# Final Project, Alexandra Sculley, v0.9

import pygame, sys, random 
from sys import exit
clock = pygame.time.Clock()
x = 800
y = 600
xButOp1, xButOp2, xButOp3 = 180, 70, 290
yButOp1, yButOp2 = 430, 540
xSlotOp1, xSlotOp2, xSlotOp3 = 740, 628, 516
gameScreenX, gameScreenY = 200, 370
playerX, playerY = 300, 300
leftCeiling, rightCeiling, floorCeiling, topCeiling =  250, 445, 259, 42

screen = pygame.display.set_mode((x, y))

class InventorySlots: # Use PascalCase for ClassNames
    def __init__(self, xValue, yValue): 
        self.xValue = xValue
        self.yValue = yValue
        self.Image = pygame.image.load('Img/slot.png')
        self.Scale = None
slot1 = InventorySlots(xSlotOp1, yButOp2)
slot2 = InventorySlots(xSlotOp2, yButOp1)
slot3 = InventorySlots(xSlotOp2, yButOp1)
slot4 = InventorySlots(xSlotOp2, yButOp2)
slot5 = InventorySlots(xSlotOp3, yButOp2)
slot6 = InventorySlots(xSlotOp3, yButOp1)

vel = 1
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    #if keys[pygame.K_w]:
    #    if playerY > 10:
    #        playerY -= vel
    #if keys[pygame.K_d]:
    #    playerX += vel
    #if keys[pygame.K_s]:
    #    playerY += vel
    #if keys[pygame.K_a]:
    #    playerX -= vel
    screen.blit(slot1, (slot1.xValue, slot1.yValue))
    #window.fill((0, 0, 0))
    pygame.display.update()