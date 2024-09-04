import pygame
from defines import *
class Block:
    width = 50
    height = 50

    def __init__(self,coord_tuple):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]
        self.block_sprite = pygame.Rect(self.x, self.y, Block.width, Block.height)


    def draw(self,screen):
        self.block_sprite = pygame.Rect(self.x, self.y, Block.width, Block.height)
        pygame.draw.rect(screen,BROWN,self.block_sprite)
        pygame.draw.rect(screen, BLACK, self.block_sprite, 1)