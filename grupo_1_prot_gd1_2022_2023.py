import pygame as py
import numpy as np
import math
from pygame.locals import *
from pygame.math import Vector2

#variaveis
Screen_x = 400
Screen_y = 800
Background = (125, 125, 125)

#main    
def main():
    py.init()
    Screen = py.display.set_mode((Screen_x, Screen_y))
    Clock = py.time.Clock()

    #ciclo de jogo
    while True:
        screen.fill(Background)
        py.display.flip()

        clock.tick(60)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
