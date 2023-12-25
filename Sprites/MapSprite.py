import pygame
from pygame.sprite import Sprite
from pygame import image
import config


class MapSprite(Sprite):
    def __init__(self, file):
        super().__init__()
        self.image = image.load("assets/" + file)
        self.rect = self.image.get_rect()

        self.is_wall = False
        self.name = ""


class Air(MapSprite):
    x = 0
    y = 0

    def __init__(self):
        super().__init__("ground.png")
        self.name = "Grass"
        self.rect.x = Air.x
        self.rect.y = Air.y
        self.is_wall = False
        self.image = pygame.Surface((config.CELL_SIZE, config.CELL_SIZE))
        Air.x += config.CELL_SIZE
        if Air.x == config.WIDTH:
            Air.x = 0
            Air.y += config.CELL_SIZE
class Grass(MapSprite):
    def __init__(self):
        super().__init__("ground.png")
        self.name = "Grass"
        self.is_wall = True


class Dirt (MapSprite):
    def __init__(self):
        super().__init__("gray.png")
        self.name = "Dirt"
        self.is_wall = True


class Stone_dirt (MapSprite):
    def __init__(self):
        super().__init__("decobel.png")
        self.name = "Stone_dirt"
        self.is_wall = True


class Stone (MapSprite):
    def __init__(self):
        super().__init__("cobel.png")
        self.name = "Stone"
        self.is_wall = True


