# KILLER GARY!111!!1 Sculley, Alexandra, v0.5

import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('KILLER GARY!1!111!!!!')
clock = pygame.time.Clock()
testFont = pygame.font.Font(None, 50)
textColor = (64,64,64)


pink = (255, 100, 200)
#testSurface = pygame.Surface((100,200))
#testSurface.fill(pink)
skySurface = pygame.image.load('Images/Sky.png').convert()
groundSurface = pygame.image.load('Images/Ground.jfif').convert()
titleSurface = testFont.render('Killer Gary', False, 'Blue')

scoreSurface = testFont.render('0', False, 'Blue')
scoreRectanlge = scoreSurface.get_rect(center = (760, 45))

snailSurface = pygame.image.load('Images/snail.png').convert_alpha()
snailRectangle = snailSurface.get_rect(midbottom = (600,300))

playerSurface = pygame.image.load('Images/Littlebro.png').convert_alpha()
playerRectangle = playerSurface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if playerRectangle.collidepoint(event.pos): print('DONT TOUCH ME')
    # draw all our elements
    # update everything
    screen.blit(skySurface, (0,0))
    screen.blit(groundSurface, (0,200))
    screen.blit(titleSurface, (325, 50))
    pygame.draw.rect(screen, pink, scoreRectanlge)
    pygame.draw.rect(screen, pink, scoreRectanlge,10)
    
    screen.blit(scoreSurface, scoreRectanlge)
    snailRectangle.x -= 4
    screen.blit(snailSurface, snailRectangle)
    if snailRectangle.right <= 0: snailRectangle.left = 800
    screen.blit(playerSurface, playerRectangle)

    # if playerRectangle.colliderect(snailRectangle):
    #     print('collision')
    # mousePos = pygame.mouse.get_pos()
    # if playerRectangle.collidepoint(mousePos):
    #     print(pygame.mouse.get_pressed())
    

    pygame.display.update()
    clock.tick(60)
