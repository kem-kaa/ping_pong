import pygame
from settings import *

import ball

pygame.init()

pygame.display.set_caption('пинг-понг')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ball.reset_ball()
                                 
running = True

while running:
    #отслеживание действий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #апдейты
    ball.update_ball()


    #отрисовка
    screen.fill((99, 8, 54))

    ball.draw_ball(screen)

    pygame.display.update()
    clock.tick(FPS)
