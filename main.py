import pygame
from data import *

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("Pong")


def run():
    game = True

    while game:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False


run()