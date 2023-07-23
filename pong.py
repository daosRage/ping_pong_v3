import pygame
from data import *


class Platform(pygame.Rect):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height)
        self.SPEED = speed
        self.MOVE = {"UP": False, "DOWN": False}
    
    def move(self, window):
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED
        elif self.MOVE["DOWN"] and self.y < setting_win["HEIGHT"] - self.height:
            self.y += self.SPEED
        pygame.draw.rect(window, (255, 255, 255), self)