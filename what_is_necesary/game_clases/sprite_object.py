from game_constants import *
from game_object import *
import pygame
import os

class Sprite_obj(Game_obj):
    """this class takes care of putting the sprite on the screen and animating it when needed"""
    sprite_display = pygame.display.set_mode((WIDTH,HEIGHT))
    def __init__(self,coord_tuple,sprites_directory):
        super.__init__(coord_tuple)
        sprites_paths = [sprites_directory + i for i in os.listdir(sprites_directory)]
        self.__sprites =[pygame.image.load(i) for i in sprites_paths]
        self.frame = 0

    def get_default_sprite(self):
        return self.__sprites[0]

    def mirror(self,offset):
        pass

    def draw(self):
        Sprite_obj.sprite_display.blit(self.__sprites[self.frame], (self.x, self.y))


    def animate(self,frames,timing):
        if self.frame in frames:
            i = frames.index(self.frame)
            if self.frame != frames[-1]:
                self.frame = frames(i+1)
            else:
                self.frame = frames[0]
        else:
            self.frame = frames[0]
