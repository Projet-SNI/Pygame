import pygame

pygame.init()

fenetre = pygame.display.set_mode((1280, 720)) # ne pas toucher!!! taille de la fenetre
pygame.display.set_caption("On test")

x = 50
y = 500
x2 = 1100
y2 = 500
width = 80
height = 100
vit = 25

saut = False
hautsaut = 12
saut2 = False
hautsaut2 = 12

run = True

while run:  # ne pas toucher!!! permet de garder le programme actif.
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    touche = pygame.key.get_pressed()
# controle perso1
    if touche[pygame.K_a] and x > vit:
        x -= vit
    if touche[pygame.K_doublea]:
        x -= 2*vit
    if touche[pygame.K_d] and x < 1280 - vit - width:
        x += vit
    if not (saut):
        if touche[pygame.K_w]:
            saut = True
    else:
        if hautsaut >= -12:
            y -= (hautsaut * abs(hautsaut)) * 0.5
            hautsaut -= 2
        else:
            hautsaut = 12
            saut = False
# controle perso2
    if touche[pygame.K_LEFT] and x2 > vit:
        x2 -= vit
    if touche[pygame.K_RIGHT] and x2 < 1280 - vit - width:
        x2 += vit
    if not (saut2):
        if touche[pygame.K_UP]:
            saut2 = True
    else:
        if hautsaut2 >= -12:
            y2 -= (hautsaut2 * abs(hautsaut2)) * 0.5
            hautsaut2 -= 2
        else:
            hautsaut2 = 12
            saut2 = False

    fenetre.fill((100, 0, 200))
    perso1 = pygame.draw.rect(fenetre, (255, 0, 0), (x, y, width, height))
    perso2 = pygame.draw.rect(fenetre, (255, 255, 255), (x2, y2, width, height))
    pygame.display.update()

pygame.quit()
