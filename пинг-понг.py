from pygame import *

run = True
game = True
finish = False

#background = transform.scale(image.load("galaxy.jpg"), (w_width,w_height))

lost = 0
max_lost=3


w_width = 700
w_height = 600
window = display.set_mode((w_width,w_height))
display.set_caption("ping-pong")
clock = time.Clock()

speed_x = 3
speed_y = 3
'''font.init()
font = font.SysFont('ComicSansMC', 50)
win_text = font.render(
    'счёт: '+str(lost), True, (255, 215, 0)
)
win_text1 = font.render(
    'пропусков: ', True, (255, 215, 0)
)
lose = font.render(
    'Ты проиграл', True, (255, 215, 0)
)'''
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
class Racket(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 535:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 535:
            self.rect.y += self.speed
    def update_ball(self):
        global speed_x
        global speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.y > w_height-50
            or self.rect.y < 0:
            speed_y *= -1
'''class T_ball(GameSprite):
    def update_ball(self):
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.y > w_height-50
            or self.rect.y < 0:
            speed_y *= -1'''

racket = Racket("racket.png", 630, 100, 50, 50, 5)
racket2 = Racket("racket.png", 20, 100, 100, 20, 5)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.fill((155, 0, 255))
        '''ball.rect.x += speed_x
        ball.rect.y += speed_y'''
        racket.update_l()
        racket.reset()
        racket2.update_r()
        racket2.reset()
    display.update()
    clock.tick(60)