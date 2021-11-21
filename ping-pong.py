from pygame import *
import pygame_menu
init()

w_width = 700
w_height = 600
window = display.set_mode((w_width,w_height))
display.set_caption("ping-pong")
clock = time.Clock()

speed_x = 4
speed_y = 4

def set_difficulty(*args):

    if args[1] == 1:
        print("Сложна")
def start_the_game():
    run = True
    game = True
    finish = False

    #background = transform.scale(image.load("galaxy.jpg"), (w_width,w_height))

    lost = 0
    max_lost=2





    #Font.init()
    font1 = font.SysFont('ComicSansMC', 50)
    win1 = font1.render(
        'Игрок 1 победил', True, (255, 215, 0)
    )
    win2 = font1.render(
        'Игрок 2 победил', True, (255, 215, 0)
    )
    score1 = font1.render(
        '0', True, (255, 215, 0))
    score2 = font1.render(
        '0', True, (255, 215, 0))
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
            if keys[K_DOWN] and self.rect.y < 500:
                self.rect.y += self.speed
        def update_r(self):
            keys = key.get_pressed()
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < 500:
                self.rect.y += self.speed
        def update_ball(self):
            global speed_x
            global speed_y
            self.rect.x += speed_x
            self.rect.y += speed_y
            if self.rect.y > w_height-50 or self.rect.y < 0:
                speed_y *= -1
    '''class T_ball(GameSprite):
        def update_ball(self):
            self.rect.x += speed_x
            self.rect.y += speed_y
            if self.rect.y > w_height-50
                or self.rect.y < 0:
                speed_y *= -1'''

    racket = Racket("racket.png", 630, 100, 95, 25, 10)
    racket2 = Racket("racket.png", 20, 100, 95, 25, 10)
    ball = Racket("tenis_ball.png", 350, 300, 25, 25, 3)
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
            ball.update()
            ball.reset()
            window.blit(score1, (320, 0))
            window.blit(score2, (370,0))
            ball.rect.x += speed_x
            ball.rect.y += speed_y
            if ball.rect.y > w_height-50 or ball.rect.y < 0:
                speed_y *= -1
            if sprite.collide_rect(racket, ball) or sprite.collide_rect(racket2, ball):
                speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(win1, (200,200))
        if ball.rect.x > 680:
            finish = True
            window.blit(win2, (200,200))
        display.update()
        clock.tick(60)
menu = pygame_menu.Menu("Привет-привет", 350, 300, theme = pygame_menu.themes.THEME_SOLARIZED)
menu.add.selector('Difficulty', [('Hard', 1), ("Easy", 2), ("Normal", 3)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT) 
menu.mainloop(window)