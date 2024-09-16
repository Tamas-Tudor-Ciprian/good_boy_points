import pygame

from defines import *

class Item:
    """completly forgot about this one but this will also need to be revamped"""

    sprite_display = pygame.display.set_mode((WIDTH,HEIGHT))
    def __init__(self,coord_tuple,offset_tuple,sprite):
        self.offset = offset_tuple
        self.x = coord_tuple[0]+self.offset[0]
        self.y = coord_tuple[1]+self.offset[1]
        self.sprite = pygame.image.load(sprite)
        self.sprite_copy = self.sprite
        self.angle = 0.0
        self.switch = True
        self.flipped = False

    def set_coords(self,coord_tuple,orientation):
        if orientation:
            self.x = coord_tuple[0] + self.offset[0]
            self.y = coord_tuple[1] + self.offset[1]
            if self.flipped:
                self.flipped = False
                self.sprite = self.sprite_copy
                self.sprite = pygame.transform.flip(self.sprite,True,False)
                self.sprite_copy = self.sprite
        else:
            self.x = coord_tuple[0] - self.offset[0]
            self.y = coord_tuple[1] + self.offset[1]
            if not self.flipped:
                self.flipped = True
                self.sprite = self.sprite_copy
                self.sprite = pygame.transform.flip(self.sprite,True,False)
                self.sprite_copy = self.sprite


    def draw(self):
        Item.sprite_display.blit(self.sprite,(self.x,self.y))



class Pickaxe(Item):
    def mine(self):
        if self.switch:
            if self.flipped:
                self.sprite = pygame.transform.rotate(self.sprite,45)
            else:
                self.sprite = pygame.transform.rotate(self.sprite, -45)
            self.switch = False
        else:
            self.sprite = self.sprite_copy
            self.switch = True
