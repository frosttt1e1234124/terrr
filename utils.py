import random
import math

from pygame.sprite import Group

import config
from Sprites.MapSprite import *

import Sprites.MapSprite


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def get_lenght(x1, y1, x2, y2):
    x = (x1 - x2) ** 2
    y = math.pow(y1 - y2, 2)
    return math.sqrt(x + y)


def generate_walls(__map):
    config.MAP_GENERATOR_TEST = config.MAP_GENERATOR_TEST[::-1]

    for y in range(config.CELL_ON_HEIGHT):
        stone, stone_dirt, dirt, grass = config.MAP_GENERATOR_TEST[y]
        p_stone = stone * config.CELL_ON_WIDTH
        p_stone_dirt = stone_dirt * config.CELL_ON_WIDTH
        p_dirt = dirt * config.CELL_ON_WIDTH
        p_grass = grass * config.CELL_ON_WIDTH

        Blocks = random.sample(
            population=[Stone, Stone_dirt, Dirt, Grass, Air],
            counts=[
                math.ceil(p_stone), math.ceil(p_stone_dirt),   math.ceil(p_dirt),  math.ceil(p_grass),
                config.CELL_ON_WIDTH - math.ceil(p_stone) - math.ceil(p_stone_dirt) - math.ceil(p_dirt) - math.ceil(p_grass)
            ],
            k=config.CELL_ON_WIDTH
        )
        random.shuffle(Blocks)

        line = []
        # for x in range(config.CELL_ON_WIDTH):
        #     air = list(__map[y])[x]
        #     block = Blocks[x]()
        #
        #     if block is not None:
        #         block.rect = air.rect
        #         line.append(block)
        #         __map[y].remove(air)
        # else:
        #     for item in line:
        #         __map[y].add(item)
        for index, item in enumerate(__map[y].sprites()):
            block = Blocks[index]()

            if block is not None:
                block.rect = item.rect
                line.append(block)
                __map[y].remove(item)
        else:
            for item in line:
                __map[y].add(item)

    #

    # while count != 128:
    #     x, y = random.randint(0, 31), random.randint(0, 31)
    #     row = list(__map[y])
    #     element = row[x]
    #
    #     if type(element) == Ground:
    #         wall = Dern()
    #         wall.rect = element.rect
    #         count += 1
    #         __map[y].remove(element)
    #         __map[y].add(wall)
