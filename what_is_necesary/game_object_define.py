
#new code standard: if I use a class that I did not make myself then that class will not be
#a parent class for any of my clases, my framework and the imported framework stay separate

import pygame
from defines import *



class Game_obj:

    def __init__(self,coord_tuple):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]

    def relocate(self,coord_tuple):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]


class Sprite_obj(Game_obj):

    sprite_display = pygame.display.set_mode((WIDTH,HEIGHT))
    def __init__(self,coord_tuple,sprites_paths):
        super.__init__(coord_tuple)
        self.sprites =[pygame.image.load(i) for i in sprites_paths]
        self.frame = 0

    def draw(self):
        Sprite_obj.sprite_display.blit(self.sprites[self.frame],(self.x,self.y))



class Rect_obj(Game_obj):
    def __init__(self,coord_tuple,height,width):
        super.__init__(coord_tuple)
        self.height = height
        self.width = width
        self.rectangle = pygame.Rect(self.x,self.y,self.height,self.width)

    def reclocate(self,coord_tuple):
        super().relocate(coord_tuple)
        self.rectangle.x = coord_tuple[0]
        self.rectangle.y = coord_tuple[0]






class Rect_sprite_obj:
    pass



class collision_obj:
    pass