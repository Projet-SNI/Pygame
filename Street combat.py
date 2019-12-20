import pygame

pygame.init()

taillefen = pygame.display.set_mode((1600, 900))  # ne pas toucher!!! taille de la fenetre
pygame.display.set_caption("Jeu")

sprite = pygame.image.load("image/mandic.png").convert_alpha()
marchegauche = [pygame.image.load('image/G1.png'), pygame.image.load('image/G2.png'), pygame.image.load('image/G3.png'),
                pygame.image.load('image/G4.png'), pygame.image.load('image/G5.png'), pygame.image.load('image/G6.png'),
                pygame.image.load('image/G7.png')]
marchedroite = [pygame.image.load('image/D1.png'), pygame.image.load('image/D2.png'), pygame.image.load('image/D3.png'),
                pygame.image.load('image/D4.png'), pygame.image.load('image/D5.png'), pygame.image.load('image/D6.png'),
                pygame.image.load('image/D7.png')]
fond = pygame.image.load("image/1.jpg")

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.saut = False
        self.g = False
        self.d = False
        self.mouv = 0
        self.mouvsaut = 10
        self.debout = True

    def draw(self, taillefen):
        if self.mouv + 1 >= 21:
            self.mouv = 0
        if not self.debout:
            if self.g:
                taillefen.blit(marchegauche[self.mouv // 3], (self.x, self.y))
                self.mouv += 1
            elif self.d:
                taillefen.blit(marchedroite[self.mouv // 3], (self.x, self.y))
                self.mouv += 1
        else:
            if self.d:
                taillefen.blit(marchedroite[0], (self.x, self.y))
            else:
                taillefen.blit(marchegauche[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 25 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def fenetre():
    taillefen.blit(fond, (0, 0))
    perso1.draw(taillefen)
    for balle in balles:
        balle.draw(taillefen)
    pygame.display.update()


# Main
perso1 = player(200, 410, 120, 234)
balles = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for balle in balles:
        if 1600 > balle.x > 0:
            balle.x += balle.vel
        else:
            balles.pop(balles.index(balle))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if perso1.g:
            facing = -1
        else:
            facing = 1
        if len(balles) < 2:
            balles.append(projectile(round(perso1.x + perso1.width // 2), round(perso1.y + perso1.height // 2), 10,
                                     (255, 255, 255), facing))

    if keys[pygame.K_a] and perso1.x > perso1.vel:
        perso1.x -= perso1.vel
        perso1.g = True
        perso1.d = False
        perso1.debout = False
    elif keys[pygame.K_d] and perso1.x < 1600 - perso1.width - perso1.vel:
        perso1.x += perso1.vel
        perso1.d = True
        perso1.g = False
        perso1.debout = False
    else:
        perso1.debout = True
        perso1.mouv = 0

    if not perso1.saut:
        if keys[pygame.K_w]:
            perso1.saut = True
            perso1.d = False
            perso1.g = False
            perso1.mouv = 0
    else:
        if perso1.mouvsaut >= -10:
            neg = 1
            if perso1.mouvsaut < 0:
                neg = -1
            perso1.y -= (perso1.mouvsaut ** 2) * 0.5 * neg
            perso1.mouvsaut -= 1
        else:
            perso1.saut = False
            perso1.mouvsaut = 10

    fenetre()

pygame.quit()
