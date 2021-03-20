import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 478

pygame.display.set_caption('Flappy Bird')

screen = pygame.display.set_mode((screen_width, screen_height))

bg = pygame.image.load("images/background.png").convert()
bird = pygame.image.load("images/bird.png").convert()
top_pip = pygame.image.load("images/top_pipe.png").convert()
bottom_pip = pygame.image.load("images/bottom_pipe.png").convert()



run = True
while run:

    clock.tick(fps)


    screen.blit(bg, (0,0))
    screen.blit(bird, (0,0))
    screen.blit(top_pip, (100,0))
    screen.blit(bottom_pip, (100,300))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
