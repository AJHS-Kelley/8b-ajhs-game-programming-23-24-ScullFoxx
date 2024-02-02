# KILLER GARY!111!!1 Sculley, Alexandra, v1.0

import pygame 
from sys import exit
def displayScore():
    currentTime = int(pygame.time.get_ticks() / 1000) - startTime
    scoreSurface = testFont.render(f'{currentTime}', False, textColor)
    scoreRectangle = scoreSurface.get_rect(center = (760, 45))
    screen.blit(scoreSurface, scoreRectangle)


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('KILLER GARY!1!111!!!!')
clock = pygame.time.Clock()
testFont = pygame.font.Font(None, 50)
textColor = (64,64,64)
gameActive = True
startTime = 0

pink = (255, 200, 200)
#testSurface = pygame.Surface((100,200))
#testSurface.fill(pink)
skySurface = pygame.image.load('Images/Sky.png').convert()
groundSurface = pygame.image.load('Images/Ground.jfif').convert()

titleSurface = testFont.render('Killer Gary', False, textColor)
titleRectangle = titleSurface.get_rect(topleft = (325,50))

# scoreSurface = testFont.render('0', False, 'Blue')
# scoreRectanlge = scoreSurface.get_rect(center = (760, 45))

deathSurface = testFont.render('GAME OVER! Restart? (PRESS SPACE)', False, 'Black')
deathRectangle = deathSurface.get_rect(topleft = (100, 50))

snailSurface = pygame.image.load('Images/snail.png').convert_alpha()
snailRectangle = snailSurface.get_rect(midbottom = (600,300))

playerSurface = pygame.image.load('Images/Littlebro.png').convert_alpha()
playerRectangle = playerSurface.get_rect(midbottom = (80,300))
playerGravity = 0

deathPlayerSurface = pygame.image.load('Images/PETER NO.jpg').convert_alpha()
deathPlayerRectangle = deathPlayerSurface.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if gameActive:
            if event.type == pygame.MOUSEBUTTONDOWN and playerRectangle.bottom >= 300:
                        playerGravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and playerRectangle.bottom >= 300:
                        playerGravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True
                snailRectangle.left = 800
                startTime = int(pygame.time.get_ticks() / 1000)

    # draw all our elements
    # update everything
    if gameActive:
        screen.blit(skySurface, (0,0))
        screen.blit(groundSurface, (0,200))
        # pygame.draw.rect(screen, '#c0e8ec', scoreRectanlge)
        # pygame.draw.rect(screen, '#c0e8ec', scoreRectanlge,10)
        pygame.draw.rect(screen, '#c0e8ec', titleRectangle)
        pygame.draw.rect(screen, '#c0e8ec', titleRectangle,10)
        screen.blit(titleSurface, titleRectangle)
        
        # screen.blit(scoreSurface, scoreRectanlge)
        displayScore()
        snailRectangle.x -= 7
        screen.blit(snailSurface, snailRectangle)
        if snailRectangle.right <= 0: snailRectangle.left = 800

        # Player
        playerGravity += 1
        playerRectangle.y += playerGravity
        if playerRectangle.bottom >= 300: playerRectangle.bottom = 300
        screen.blit(playerSurface, playerRectangle)

        # collision
        if snailRectangle.colliderect(playerRectangle):
            gameActive = False
    else:
        screen.blit(skySurface, (0,0))
        screen.blit(deathPlayerSurface, deathPlayerRectangle)
        screen.blit(deathSurface, deathRectangle)




    

    pygame.display.update()
    clock.tick(60)
