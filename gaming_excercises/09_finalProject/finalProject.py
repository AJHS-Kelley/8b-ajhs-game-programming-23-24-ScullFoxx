# Final Project, Alexandra Sculley, v0.0

import pygame, sys, random 
from sys import exit

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

pygame.init()

difficulty = int(input("Please select a difficulty. Enter 1 for Short Dungeon and 2 for Long Dungeon\n"))

if difficulty == 1:
    z = "Dungeon Explorer: Short dungeon"
else:
    z = "Dungeon Explorer: Long dungeon"

pygame.display.set_caption(z)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
