import pygame

from defines import *

class Item:

    sprite_display = pygame.display.set_mode((WIDTH,HEIGHT))
    def __init__(self,coord_tuple,offset_tuple,sprite):
        self.offset = offset_tuple
        self.x = coord_tuple[0]+self.offset[0]
        self.y = coord_tuple[1]+self.offset[1]
        self.sprite = pygame.image.load(sprite)
        self.sprite_copy = self.sprite
        self.angle = 0.0
        self.switch = True

    def set_coords(self,coord_tuple):
        self.x = coord_tuple[0] + self.offset[0]
        self.y = coord_tuple[1] + self.offset[1]

    def draw(self):
        Item.sprite_display.blit(self.sprite,(self.x,self.y))



class Pickaxe(Item):
    def mine(self):
        if self.switch:
            self.sprite = pygame.transform.rotate(self.sprite,-45)
            self.switch = False
        else:
            self.sprite = self.sprite_copy
            self.switch = True
