import math, random, sys
import pygame
import pygame.gfxdraw
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock()
FPS = 120

pygame.display.set_caption('Jump Bird')

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DW_HALF = DISPLAY_WIDTH/2
DH_HALF = DISPLAY_HEIGHT/2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT

DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

bird = pygame.image.load('images/bird.png')
bird_dim = bird.get_rect()
bg = pygame.image.load('images/background.png').convert()
bg_width, bg_height = bg.get_rect().size
top_pip = pygame.image.load("images/top_pipe.png").convert()
bottom_pip = pygame.image.load("images/bottom_pipe.png").convert()
middle_pip = pygame.image.load("images/middle_pipe.png").convert()


direction = -1
x = DW_HALF - bird_dim.center[0]

class player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.jumping = False
        self.jump_offset = 0


birdy = player(DW_HALF, DH_HALF, 30)
jump_height = 50

def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
            pygame.quit()
            sys.exit()

def keys(player):
    keys = pygame.key.get_pressed()
    if keys[K_SPACE] and player.jumping == False: #and player.jump_offset == 0:
        player.jumping = True

def do_jumping(player):
    global jump_height

    if player.jumping:
        player.jump_offset += 3
        if player.jump_offset >= jump_height:
            player.jumping = False
    elif player.jump_offset > 0 and player.jumping == False:
        player.jump_offset -= 1



while True:
    event_handler()

    keys(birdy)
    do_jumping(birdy)

    DS.blit(bg, (0,0))
    #DS.blit(top_pip, (800,100))
    #DS.blit(bottom_pip, (800,400))

    #pygame.draw.rect(DS, (255,255,255), (250,250, DISPLAY_WIDTH /2, DISPLAY_HEIGHT /2),0)
    #pygame.draw.circle(DS, (255,255,255), (birdy.x, birdy.y - birdy.jump_offset), 50 , 0)

    DS.blit(bird, (birdy.x, 500 - birdy.jump_offset))
    DS.blit(top_pip, (x, DH_HALF - 125))
    DS.blit(bottom_pip, (x, DH_HALF - -175))
    DS.blit(middle_pip, (x, DH_HALF - 400))

    DS.blit(top_pip, (x + 300, DH_HALF - 200))
    DS.blit(bottom_pip, (x + 300, DH_HALF - -100))
    DS.blit(middle_pip, (x + 300, DH_HALF - 400))
    DS.blit(middle_pip, (x + 300, DH_HALF - -150))

    DS.blit(top_pip, (x + 600, DH_HALF - 125))
    DS.blit(bottom_pip, (x + 600, DH_HALF - -175))
    DS.blit(middle_pip, (x + 600, DH_HALF - 400))
    
    DS.blit(top_pip, (x + 900, DH_HALF - 200))
    DS.blit(bottom_pip, (x + 900, DH_HALF - -100))
    DS.blit(middle_pip, (x + 900, DH_HALF - 400))
    DS.blit(middle_pip, (x + 900, DH_HALF - -150))

    DS.blit(top_pip, (x + 1200, DH_HALF - 200))
    DS.blit(bottom_pip, (x + 1200, DH_HALF - -100))
    DS.blit(middle_pip, (x + 1200, DH_HALF - 400))
    DS.blit(middle_pip, (x + 1200, DH_HALF - -150))

    DS.blit(top_pip, (x + 1500, DH_HALF - 125))
    DS.blit(bottom_pip, (x + 1500, DH_HALF - -175))
    DS.blit(middle_pip, (x + 1500, DH_HALF - 400))

    DS.blit(top_pip, (x + 1800, DH_HALF - 200))
    DS.blit(bottom_pip, (x + 1800, DH_HALF - -100))
    DS.blit(middle_pip, (x + 1800, DH_HALF - 400))
    DS.blit(middle_pip, (x + 1800, DH_HALF - -150))

    DS.blit(top_pip, (x + 2100, DH_HALF - 125))
    DS.blit(bottom_pip, (x + 2100, DH_HALF - -175))
    DS.blit(middle_pip, (x + 2100, DH_HALF - 400))

    DS.blit(top_pip, (x + 2400, DH_HALF - 125))
    DS.blit(bottom_pip, (x + 2400, DH_HALF - -175))
    DS.blit(middle_pip, (x + 2400, DH_HALF - 400))

    DS.blit(top_pip, (x + 2700, DH_HALF - 200))
    DS.blit(bottom_pip, (x + 2700, DH_HALF - -100))
    DS.blit(middle_pip, (x + 2700, DH_HALF - 400))
    DS.blit(middle_pip, (x + 2700, DH_HALF - -150))

    DS.blit(top_pip, (x + 3000, DH_HALF - 125))
    DS.blit(bottom_pip, (x + 3000, DH_HALF - -175))
    DS.blit(middle_pip, (x + 3000, DH_HALF - 400))
    
    x += direction


    #if x >= DISPLAY_WIDTH - bird_dim.width or x <= 0:
    #    direction *= 1


    pygame.display.update()
    clock.tick(FPS)
    
    DS.fill([0,0,0])