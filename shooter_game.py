from pygame import *
from random import randint
import time as t
speed_p = 7
lost = 0
score = 0
score1 = 0
max_lost=3
w_width = 700
w_height = 600
window = display.set_mode((w_width,w_height))
display.set_caption("htpyz")
background = transform.scale(image.load("galaxy.jpg"), (w_width,w_height))
game = True
num_fire = 0
rel_time = False
clock = time.Clock()

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
font.init()
font = font.SysFont('ComicSansMC', 50)
win_text = font.render(
    'счёт: '+str(lost), True, (255, 215, 0)
)
win_text1 = font.render(
    'пропусков: ', True, (255, 215, 0)
)
lose = font.render(
    'Ты проиграл', True, (255, 215, 0)
)
class GameSprite(sprite.Sprite):
    def __init__(self, playerimage, playerx, playery, spr_width, spr_height, playerspeed):
        super().__init__()
        self.image = transform.scale(image.load(playerimage), (spr_height, spr_width))
        self.speed = playerspeed
        self.rect = self.image.get_rect()
        self.rect.x = playerx
        self.rect.y = playery
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[K_DOWN]:
            self.rect.x = 330
        if keys[K_BACKSPACE]:
            global finish
            finish = True
            window.blit(lose, (200,200))
        if keys[K_QUESTION]:
            self.rect.x = 100
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top,25,15, 15)
        bullets.add(bullet)
class Monster(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > w_height:
            self.rect.x = randint(80, w_width - 80)
            self.rect.y = 0
            lost = lost + 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
class Asteroid(Monster):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > w_height:
            self.rect.x = randint(80, w_width - 80)
            self.rect.y = 0
            lost = lost + 1

bullets = sprite.Group()   

asteroids = sprite.Group()

img_ast = 'asteroid.png'
img_enemy = "ufo.png"
player = Player("rocket.png", 5, 500,65, 45, speed_p)
monsters = sprite.Group()
for i in range (1,6):
    monster = Monster(img_enemy, randint(80, w_width-80), -40,65, 65,randint(1,3))
    monsters.add(monster)
for i in range (1, 3):
    asteroid = Asteroid(img_ast, randint(80, w_width-80), - 40,65, 65, randint(1,5))
    asteroids.add(asteroid)
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    
                    #fire_sound.play()
                    num_fire = num_fire + 1
                    player.fire()
                if num_fire >= 5 and rel_time == False:
                    last_time = t.time()
                    rel_time = True
    if not finish:
        window.blit(background, (0, 0))
        player.reset()
        player.update()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        asteroids.update()
        asteroids.draw(window)
        if rel_time == True:
            now_timer = t.time()
            if now_timer - last_time < 0.3:
                reload = font.render('one sec', 1, (150, 0, 0))
                window.blit(reload, (250, 500))
            else:
                num_fire = 0
                rel_time = False
        collides = sprite.groupcollide(monsters, bullets, True, True)
        colides1 = sprite.spritecollide(player, asteroids, False)
        colides2 = sprite.groupcollide(asteroids, bullets, False, True)        

        for c in collides:
            score += 1
            monster = Monster(img_enemy, randint(80, w_width -  80), -40, 65, 65, randint(1,3))
            monsters.add(monster)
        if sprite.spritecollide(player, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))
        if sprite.spritecollide(player, asteroids, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))
        
        
        display.update()
        clock.tick(60)