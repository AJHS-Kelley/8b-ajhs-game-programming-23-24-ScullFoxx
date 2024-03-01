# Just want an egg clicker for right now v0.6

import pygame 
from sys import exit
pygame.init()
eggPress = 0
startTime = 0

screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
gameActive = True
pygame.display.set_caption('Egg Clicker!')
textFont = pygame.font.Font(None, 50)

def displayTimer():
    currentTimer = int(pygame.time.get_ticks() / 1000)
    timerSurface = textFont.render(f'{currentTimer}', False, (255,255,255))
    timerRectangle = timerSurface.get_rect(center = (400, 300))
    screen.blit(timerSurface, timerRectangle)

# Money/Score


# Egg
eggSurface = pygame.image.load('Images/Egg.png')
eggSurface = pygame.transform.rotozoom(eggSurface, 1, 2.5)
eggRect = eggSurface.get_rect(center = (400,200))

# Game Text
gamSurf = textFont.render('Please click the egg as much in 10 seconds!', False, (255, 255, 255))
gamRect = gamSurf.get_rect(center = (400, 350))

# Restart
resSurf = textFont.render('Please press space to click the egg again!', False, (255, 255, 255))
resRect = resSurf.get_rect(center = (400, 300))

while True:
    moneySurface = textFont.render(f'{eggPress}', False, (255, 255, 255))
    moneyRect = moneySurface.get_rect(center = (395,50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if gameActive:
           if event.type == pygame.MOUSEBUTTONDOWN:
            if eggRect.collidepoint(event.pos):
                eggPress += 1
                #print(eggPress)
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True
                startTime = int(pygame.time.get_ticks() / 1000)
                eggPress = 0
            

    # draw all our elements
    # update everything
    if gameActive:
        screen.fill((100, 135, 155))
        displayTimer()
        screen.blit(eggSurface, eggRect)
        screen.blit(moneySurface, moneyRect)
        screen.blit(gamSurf, gamRect)
        if eggPress == 25:
            gameActive = False

    else:
        screen.fill((30,30,30))
        winSurface = textFont.render(f'You have clicked the egg {eggPress} times! Eggscellent!', False, (255, 255, 255))
        winRect = winSurface.get_rect(center = (395, 50))
        screen.blit(winSurface, winRect)
        screen.blit(resSurf, resRect)





    

    pygame.display.update()
    clock.tick(60)
