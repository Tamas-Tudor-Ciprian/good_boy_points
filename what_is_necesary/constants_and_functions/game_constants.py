import pygame

WIDTH = 1000

HEIGHT = 500

BLOCK_SIDE = 50

BLOCK_COORD = tuple((i, j)for j in range(HEIGHT - BLOCK_SIDE, -BLOCK_SIDE, -BLOCK_SIDE) for i in range(0, WIDTH , BLOCK_SIDE) )

DETECTOR_RECTANGLES = tuple(pygame.Rect(i[0],i[1],BLOCK_SIDE,BLOCK_SIDE) for i in BLOCK_COORD)

BLACK = (0,0,0)
GREY = (174,174,174)
BROWN= (196,98,16)
SKY_COLOR = (0, 255, 230)
CHARACTER_COLOR = (255, 179, 0)


SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])


COLORS = {
    "BLACK":(0,0,0),
    "GREY":(174,174,174),
    "BROWN":(196,98,16),
    "LIGHT_BLUE":(0,155,230),
    "ORANGE":(255,179,0),
    "GREEN":(0,255,0),
    "RED":(255,0,0)
}
