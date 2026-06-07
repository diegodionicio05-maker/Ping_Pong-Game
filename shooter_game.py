# ¡Crea tu propio juego de disparos!

from pygame import *
from random import randint
from time import time as tiempo
init()
mixer.init()
#mixer.music.load('name_entry_top_firstloop.wav')
#mixer.music.play()
#fire = mixer.Sound('fire.wav')
#kick = mixer.Sound('goei_destroy.wav')
#kick_n = mixer.Sound('zako_destroy.wav')

# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def reset(self, hitbox = False):
        window.blit(self.image, (self.rect.x, self.rect.y))
        if hitbox: draw.rect(window, (255, 0, 0), self.rect, 1)

class DinamicSprites(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed = 0):
        super().__init__(player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
# clase del jugador principal
class Player(DinamicSprites):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed = 0):
        super().__init__(player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def move(self, speedx):
        self.speed = speedx

    def update(self):
        self.rect.x += self.speed

    #def fire(self):
        #global bullets
        #fire.play()
        #ullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 12, 30, 5)
        #bullet.rect.centerx = self.rect.centerx
        #bullets.add(bullet)
        #return bullet

class Ball(DinamicSprites):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed = 0):
        super().__init__(player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def move(self, speedy):
        self.speed = speedy

    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.top >= 500:
            self.rect.x = randint(0,420)
            self.rect.y = -45
            self.speed = randint(1,6)
            lost += 1

#class Bullet(DinamicSprites):
    #def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed=5):
        #super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)

    #def update(self):
        #self.rect.y -= self.speed

         
window = display.set_mode((700, 500))
display.set_caption('Tirador')
bg = (225, 225, 225)

clock = time.Clock()
monsters = sprite.Group()
bullets = sprite.Group()


#player = Player('prue.png', 300, 420, 65, 65, 0)

#for i in range(5):
#    monsters.add(Enemy("ufo.png", randint(0,630), 0, 70, 45, randint(1,4)))

lost = 0
score = 0
txt_font = font.SysFont('Arial', 40)
msg_lost = txt_font.render('FALLOS: ' + str(lost), True, (255, 255, 255))
msg_score = txt_font.render('PUNTAJE: ' + str(lost), True, (255, 255, 255))
ball = Ball('basketball.png',150, 150, 65, 65, 0)
i = 0
run = True
timeshot = tiempo()
k = tiempo()
victory = font.SysFont('Arial', 80).render('FELICIDADES\nGANASTE', True, (0, 255, 0))
lose = font.SysFont('Arial', 80).render('FELICIDADES\nPERDISTE', True, (255, 0, 0))
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    msg_lost = txt_font.render('FALLOS: ' + str(lost), True, (255, 255, 255))
    msg_score = txt_font.render('PUNTAJE: ' + str(score), True, (255, 255, 255))
    
    window.fill(bg)
    ball.update()
    ball.reset()
    
    window.blit(msg_lost, (30, 30))
    window.blit(msg_score, (30, 80))
    clock.tick(40)
    if score >= 10:
        window.blit(victory, (15, 270))
    elif lost >= 3:
        window.blit(lose, (15, 270))            
    i += 1
        #if i == 405:
            #mixer.music.play()
            #i = 0
    display.update()