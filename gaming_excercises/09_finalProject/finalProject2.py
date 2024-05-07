# Final Project, Alexandra Sculley, v0.9

import pygame, sys, random, pygame.freetype
from sys import exit
clock = pygame.time.Clock()
#textFont = pygame.font.Font(None, 50)
pygame.init()
PURPLE = (53, 43, 66) 
textFont = pygame.font.Font('Fonts/Kenney Rocket.ttf', 50)

x = 1318
y = 1080
xSlotOp1, xSlotOp2, xSlotOp3 = 1020, 860, 700
gameScreenX, gameScreenY = 600, 730
leftCeiling, rightCeiling, floorCeiling, topCeiling =  700, 1130, 478, 78

startText = textFont.render('Dungeon Crawler', False, (255,255,255))

screen = pygame.display.set_mode((x, y))

class InventorySlots: # Inventory Slots
    def __init__(self, xValue, yValue): 
        self.xValue = xValue
        self.yValue = yValue
        self.Image = pygame.image.load('Img/slot.png')
        self.Scale = None

class ItemInteractions: # Such as doors, and pickups
    def __init__(self, xValue, yValue):
        self.xValue = xValue
        self.yValue = yValue

# Surfaces
slot1 = InventorySlots(xSlotOp1, 760)
slot2 = InventorySlots(xSlotOp1, 920)
slot3 = InventorySlots(xSlotOp2, 920)
slot4 = InventorySlots(xSlotOp2, 760)
slot5 = InventorySlots(xSlotOp3, 760)
slot6 = InventorySlots(xSlotOp3, 920)
gameScreen = pygame.image.load('img/DungeonRoom.png')
interactionPanel = pygame.image.load("img/InteractionBox.png")

# Player
playerStatus = "DOWN"
playerX, playerY = 900, 200

# Rectangles
gameRect = gameScreen.get_rect(bottomleft = (gameScreenX, gameScreenY))
vel = 5
run = True
while run:
    gameLevel = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if gameLevel == 1:
        screen.fill((0,0,255))
        screen.blit(startText, (0,0))
        #screen.blit(slot1.Image, (slot1.xValue, slot1.yValue))
        #playerSurf = pygame.image.load("img/playerDOWN.png")
        #screen.blit(playerSurf, (playerX, playerY))
    elif gameLevel == 2:
        if playerStatus == "DOWN":
            playerPosition = "img/playerDOWN.png"
            #print(playerPosition)
        elif playerStatus == "UP":
            playerPosition = "img/playerUP.png"
            #print(playerPosition)
        elif playerStatus == "LEFT":
            playerPosition = "img/playerLEFT.png"
            #print(playerPosition)
        elif playerStatus == "RIGHT":
            playerPosition = "img/playerRIGHT.png"
            #print(playerPosition)
        
        playerSurf = pygame.image.load(playerPosition)
        playerSurf = pygame.transform.rotozoom(playerSurf, 1.0, 2.0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            playerStatus = "UP"
            #print(playerStatus)
            if playerY > topCeiling:
                playerY -= vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            playerStatus = "RIGHT"
            #print(playerStatus)
            if playerX < rightCeiling:    
                playerX += vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            playerStatus = "DOWN"
            #print(playerStatus)
            if playerY < floorCeiling:
                playerY += vel
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            playerStatus = "LEFT"
            #print(playerStatus)
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
        screen.blit(interactionPanel, (0, 0))
        screen.blit(playerSurf, (playerX, playerY))
        #window.fill((0, 0, 0))
    pygame.display.update()