import pygame
from data import *
from pong import *

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("Pong")


def run():
    game = True
    board_left = Platform(
        10, 
        setting_win["HEIGHT"] // 2 - setting_board["HEIGHT"] // 2,
        setting_board["WIDTH"],
        setting_board["HEIGHT"],
        5)
    clock = pygame.time.Clock()

    while game:
        window.fill((0, 0, 0))
        pygame.draw.line(window, (255, 255, 255), (setting_win["WIDTH"] // 2 - 1, 0), (setting_win["WIDTH"] // 2 - 1, setting_win["HEIGHT"]), 2)

        board_left.move(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    board_left.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    board_left.MOVE["DOWN"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    board_left.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    board_left.MOVE["DOWN"] = False
            

        clock.tick(60)
        pygame.display.flip()


run()