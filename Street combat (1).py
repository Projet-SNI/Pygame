import pygame

pygame.init()

taillefen = pygame.display.set_mode((1600, 900)) # ne pas toucher!!! taille de la fenetre
pygame.display.set_caption("On test")

sprite = pygame.image.load("image/mandic.png").convert_alpha()
marchegauche = [pygame.image.load('image/G1.png'), pygame.image.load('image/G2.png'), pygame.image.load('image/G3.png'),pygame.image.load('image/G4.png'), pygame.image.load('image/G5.png'), pygame.image.load('image/G6.png'), pygame.image.load('image/G7.png')]
marchedroite =[pygame.image.load('image/D1.png'), pygame.image.load('image/D2.png'), pygame.image.load('image/D3.png'), pygame.image.load('image/D4.png'), pygame.image.load('image/D5.png'), pygame.image.load('image/D6.png'), pygame.image.load('image/D7.png')]
fond = pygame.image.load("image/1.jpg")

clock = pygame.time.Clock()

music = pygame.mixer.music.load("sound/music background.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

provocation = pygame.mixer.Sound("sound/omae-wa-mou-shindeiru.wav")
pas = pygame.mixer.Sound("sound/pas.wav")

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

    def draw(self, taillefen):
        if self.mouv + 1 >= 21:
            self.mouv = 0
        if self.g:
            taillefen.blit(marchegauche[self.mouv // 3], (self.x, self.y))
            self.mouv += 1
        elif self.d:
            taillefen.blit(marchedroite[self.mouv // 3], (self.x, self.y))
            self.mouv += 1
        else:
            taillefen.blit(sprite, (self.x, self.y))


def fenetre():
    taillefen.blit(fond, (0, 0))
    perso1.draw(taillefen)
    pygame.display.update()

perso1 = player(200, 410, 120, 234)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and perso1.x > perso1.vel:
        perso1.x -= perso1.vel
        perso1.g = True
        perso1.d = False
        pas.play()
        pas.set_volume(0.03)
    elif keys[pygame.K_d] and perso1.x < 1600 - perso1.width - perso1.vel:
        perso1.x += perso1.vel
        perso1.d = True
        perso1.g = False
        pas.play()
        pas.set_volume(0.03)
    elif keys[pygame.K_l]:
        provocation.play()
        provocation.set_volume(0.15)
    else:
        perso1.d = False
        perso1.g = False
        perso1.mouv = 0

    if not (perso1.saut):
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