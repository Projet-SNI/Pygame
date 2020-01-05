import pygame

pygame.init()

taillefen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # ne pas toucher!!! taille de la fenetre
pygame.display.set_caption("Jeu")

M_deboutgauche = pygame.image.load('image/mandicG.png')
M_deboutdroite = pygame.image.load("image/mandicD.png")
M_marchegauche = [pygame.image.load('image/G1.png'), pygame.image.load('image/G2.png'),
                  pygame.image.load('image/G3.png'),
                  pygame.image.load('image/G4.png'), pygame.image.load('image/G5.png'),
                  pygame.image.load('image/G6.png'),
                  pygame.image.load('image/G7.png'), pygame.image.load('image/G8.png')]
M_marchedroite = [pygame.image.load('image/D1.png'), pygame.image.load('image/D2.png'),
                  pygame.image.load('image/D3.png'), pygame.image.load('image/D4.png'),
                  pygame.image.load('image/D5.png'),
                  pygame.image.load('image/D6.png'), pygame.image.load('image/D7.png'),
                  pygame.image.load('image/D8.png')]

L_deboutgauche = pygame.image.load('image/mandicG.png')
L_deboutdroite = pygame.image.load("image/mandicD.png")
L_marchegauche = [pygame.image.load('image/G1.png'), pygame.image.load('image/G2.png'),
                  pygame.image.load('image/G3.png'),
                  pygame.image.load('image/G3.png'), pygame.image.load('image/G4.png'),
                  pygame.image.load('image/G5.png'),
                  pygame.image.load('image/G6.png'), pygame.image.load('image/G7.png')]
L_marchedroite = [pygame.image.load('image/D1.png'), pygame.image.load('image/D2.png'),
                  pygame.image.load('image/D3.png'), pygame.image.load('image/D4.png'),
                  pygame.image.load('image/D5.png'),
                  pygame.image.load('image/D6.png'), pygame.image.load('image/D7.png'),
                  pygame.image.load('image/D8.png')]

fond = pygame.image.load("image/1.png")

clock = pygame.time.Clock()

score1 = 0
score2 = 0

music = pygame.mixer.music.load("sound/music background.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.15)

provoc_mandic = pygame.mixer.Sound("sound/omae-wa-mou-shindeiru.wav")
provoc_lopato = pygame.mixer.Sound("sound/lopato.wav")
pas = pygame.mixer.Sound("sound/pas.wav")


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.saut = False
        self.g = False
        self.d = False
        self.mouv = 0
        self.mouvsaut = 12
        self.debout = True
        self.hitbox = (self.x, self.y, 110, 220)
        self.health = 10
        self.visible = True

    def draw(self, taillefen):
        if self.visible:
            if self.mouv + 1 >= 24:
                self.mouv = 0
            if not self.debout:
                if self.d:
                    taillefen.blit(M_marchedroite[self.mouv // 3], (self.x, self.y))
                    self.mouv += 1
                elif self.g:
                    taillefen.blit(M_marchegauche[self.mouv // 3], (self.x, self.y))
                    self.mouv += 1
            else:
                if self.g:
                    taillefen.blit(M_deboutgauche, (self.x, self.y))
                else:
                    taillefen.blit(M_deboutdroite, (self.x, self.y))
            pygame.draw.rect(taillefen, (255, 0, 0), (30, 90, 100, 30))
            pygame.draw.rect(taillefen, (0, 255, 0), (30, 90, 100, 30))
            self.hitbox = (self.x + 12, self.y + 9, 180, 230)
            # pygame.draw.rect(taillefen, (255, 0, 0), self.hitbox, 1)

    def hit(self):
        if self.health > 0:
            self.health -= 1
        print('hit')


class enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.saut = False
        self.g = False
        self.d = False
        self.mouv = 0
        self.mouvsaut = 12
        self.debout = True
        self.hitbox = (self.x, self.y, 110, 220)
        self.health = 10
        self.visible = True

    def draw(self, taillefen):
        if self.visible:
            if self.mouv + 1 >= 24:
                self.mouv = 0
            if not self.debout:
                if self.g:
                    taillefen.blit(L_marchegauche[self.mouv // 3], (self.x, self.y))
                    self.mouv += 1
                elif self.d:
                    taillefen.blit(L_marchedroite[self.mouv // 3], (self.x, self.y))
                    self.mouv += 1
            else:
                if self.d:
                    taillefen.blit(L_deboutdroite, (self.x, self.y))
                else:
                    taillefen.blit(L_deboutgauche, (self.x, self.y))
            pygame.draw.rect(taillefen, (255, 0, 0), (1000, 90, 100, 30))
            pygame.draw.rect(taillefen, (0, 255, 0), (1000, 90, 100, 30))
            self.hitbox = (self.x + 12, self.y + 9, 180, 230)
            # pygame.draw.rect(taillefen, (255, 0, 0), self.hitbox, 1)

    def hit(self):
        print('hit')


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


class projectile2(object):
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
    text = font.render('Score :' + str(score1), 1, (0, 0, 0))
    text2 = font.render('Score :' + str(score2), 1, (0, 0, 0))
    taillefen.blit(text, (30, 30))
    taillefen.blit(text2, (1000, 30))
    perso1.draw(taillefen)
    perso2.draw(taillefen)
    for balle1 in balles1:
        balle1.draw(taillefen)
    for balle2 in balles2:
        balle2.draw(taillefen)
    pygame.display.update()


# Main
font = pygame.font.SysFont('comicsans', 70, True)
perso1 = player(75, 410, 180, 234)
perso2 = enemy(1100, 410, 180, 234)
balles1 = []
balles2 = []
shootLoop = 0

run = True

while run:
    clock.tick(27)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for balle1 in balles1:
        if balle1.y - balle1.radius < perso2.hitbox[1] + perso2.hitbox[3] and balle1.y + balle1.radius > perso2.hitbox[
            1]:
            if balle1.x + balle1.radius > perso2.hitbox[0] and balle1.x - balle1.radius < perso2.hitbox[0] + \
                    perso2.hitbox[2]:
                perso2.hit()
                score1 += 1
                balles1.pop(balles1.index(balle1))
        if 1200 > balle1.x > 0:
            balle1.x += balle1.vel
        else:
            balles1.pop(balles1.index(balle1))

    for balle2 in balles2:
        if balle2.y - balle2.radius < perso1.hitbox[1] + perso1.hitbox[3] and balle2.y + balle2.radius > perso1.hitbox[
            1]:
            if balle2.x + balle2.radius > perso1.hitbox[0] and balle2.x - balle2.radius < perso1.hitbox[0] + \
                    perso1.hitbox[2]:
                perso1.hit()
                score2 += 1
                balles2.pop(balles2.index(balle2))
        if 1600 > balle2.x > 0:
            balle2.x += balle2.vel
        else:
            balles2.pop(balles2.index(balle2))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if perso1.g:
            facing = -1
        else:
            facing = 1
        if len(balles1) < 5:
            balles1.append(projectile(round(perso1.x + perso1.width // 2), round(perso1.y + perso1.height // 2), 10,
                                      (255, 255, 255), facing))

    if keys[pygame.K_a] and perso1.x > perso1.vel:
        perso1.x -= perso1.vel
        perso1.g = True
        perso1.d = False
        perso1.debout = False
        pas.play()
        pas.set_volume(0.03)
    elif keys[pygame.K_d] and perso1.x < 1280 - perso1.width - perso1.vel:
        perso1.x += perso1.vel
        perso1.d = True
        perso1.g = False
        perso1.debout = False
        pas.play()
        pas.set_volume(0.03)
    elif keys[pygame.K_l]:
        provoc_mandic.play()
        provoc_mandic.set_volume(0.10)
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
        if perso1.mouvsaut >= -12:
            neg = 1
            if perso1.mouvsaut < 0:
                neg = -1
            perso1.y -= (perso1.mouvsaut ** 2) * 0.5 * neg
            perso1.mouvsaut -= 1
        else:
            perso1.saut = False
            perso1.mouvsaut = 12

    if keys[pygame.K_m]:
        if perso2.g:
            facing = 1
        else:
            facing = -1
        if len(balles2) < 5:
            balles2.append(projectile2(round(perso2.x + perso2.width // 2), round(perso2.y + perso2.height // 2), 10,
                                       (255, 255, 255), facing))

    if keys[pygame.K_LEFT] and perso2.x > perso2.vel:
        perso2.x -= perso2.vel
        perso2.g = True
        perso2.d = False
        perso2.debout = False
        pas.play()
        pas.set_volume(0.03)
    elif keys[pygame.K_RIGHT] and perso2.x < 1280 - perso2.width - perso2.vel:
        perso2.x += perso1.vel
        perso2.d = True
        perso2.g = False
        perso2.debout = False
        pas.play()
        pas.set_volume(0.03)
    elif keys[pygame.K_KP1]:
        provoc_lopato.play()
        provoc_lopato.set_volume(0.50)
    else:
        perso2.debout = True
        perso2.mouv = 0

    if not perso2.saut:
        if keys[pygame.K_UP]:
            perso2.saut = True
            perso2.d = False
            perso2.g = False
            perso2.mouv = 0
    else:
        if perso2.mouvsaut >= -12:
            neg = 1
            if perso2.mouvsaut < 0:
                neg = -1
            perso2.y -= (perso2.mouvsaut ** 2) * 0.5 * neg
            perso2.mouvsaut -= 1
        else:
            perso2.saut = False
            perso2.mouvsaut = 12

    fenetre()

pygame.quit()
