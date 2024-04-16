import pygame

pygame.init()
window = pygame.display.set_mode(((500, 500)))
pygame.display.set_caption(("First Game"))
slotSurf = pygame.image.load('img/slot.png')
gameScreen = pygame.image.load('img/DungeonRoom.png')

playerX, playerY = 50, 50
gameScreenX, gameScreenY = 1, 1
width, height = 40, 60
vel = 1

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if playerY > 10:
            playerY -= vel
    if keys[pygame.K_d]:
        playerX += vel
    if keys[pygame.K_s]:
        playerY += vel
    if keys[pygame.K_a]:
        playerX -= vel

    #window.fill((0, 0, 0))
    window.blit(gameScreen, (gameScreenX, gameScreenY))
    window.blit(slotSurf, (playerX, playerY))
    pygame.display.update()