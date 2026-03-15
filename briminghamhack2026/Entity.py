import math

import pygame as py
from random import randint

from pygame.examples.scroll import zoom_factor


class Entity(py.sprite.Sprite):
    def __init__(self, speed: int, zoomFactor: int, sprites: list, position: list = [0,0,0]):
        super().__init__()
        self.sprites = sprites
        self.position = position #x,y,z format
        self.speed = speed
        self.zoomFactor = zoomFactor
        self.holdImage = self.sprites[0]

        self.image = self.holdImage
        self.rect = self.image.get_rect()

    def calcLayer(self, value):
        min = 2.6427579737335836
        max = 3.870422138836773
        scale = (10)/(max-min)
        return math.ceil((value - min)*scale)



    def move(self, direction):
        if direction == "up":
            self.position[1] -= self.speed
            self.position[2] -= self.speed * self.zoomFactor
        elif direction == "down":
            self.position[1] += self.speed
            self.position[2] += self.speed * self.zoomFactor
        elif direction == "left":
            self.position[0] -= self.speed
        elif direction == "right":
            self.position[0] += self.speed
