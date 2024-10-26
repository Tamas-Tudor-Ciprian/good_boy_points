from game_constants import *
from game_object import *
from math_stuff import find_element_and_continue
import pygame
import os

class Sprite_obj(Game_obj):
    """this class takes care of putting the sprite on the screen and animating it when needed"""
    sprite_display = pygame.display.set_mode((WIDTH,HEIGHT))
    def __init__(self,coord_tuple,sprites_directory):
        super().__init__(coord_tuple)
        sprites_directory = os.getcwd() +r"\\game_objects\\"+ sprites_directory
        sprites_paths = [sprites_directory  + r"\\" + i for i in os.listdir(sprites_directory)]
        self.__sprites =[pygame.image.load(i) for i in sprites_paths]
        self.current_sprite_index = 0
        self.__current_sprite = self.__sprites[self.current_sprite_index]
        self.inverted = False


    def get_sprite_nr(self):
        return len(self.__sprites)




    def rotate(self,angle):
        self.__current_sprite = pygame.transform.rotate(self.__current_sprite,angle)


    #I might add the option to scale the sprite for this function
    def get_sprite(self):
        """getter"""
        return self.__current_sprite


    def change_frame(self,frame):
        """in case you need to change the sprite instantly"""
        self.current_sprite_index = frame
        self.__current_sprite = self.__sprites[self.current_sprite_index]
        self.inverted = False
    def mirror(self,x_bool,y_bool):
        """call the pygame flip function to flip either verticaly or horizontaly as called
        though this being called each frame might not be the most eficient"""
        self.__current_sprite = pygame.transform.flip(self.__current_sprite,x_bool,y_bool)
        self.inverted = True

    def scale(self,scaling_tuple):
        """this scales the sprite,though it might not be the most eficient to do this every frame"""
        self.__current_sprite = pygame.transform.scale(self.__current_sprite,scaling_tuple)

    def draw(self):
        """we simply display the sprite with this one"""
        Sprite_obj.sprite_display.blit(self.__current_sprite, (self.x, self.y))

    def animate(self,frames,timing):
        """this here function when called will alternate the current sprite
        between the frames specified when the timing is true
        it might make a lot of sense to use a generator function to make everythin more python-y
        """
        #this solution is remarkably simple
        if timing:
            self.current_sprite_index = find_element_and_continue(self.current_sprite_index, frames)
            self.__current_sprite = self.__sprites[self.current_sprite_index]
            self.inverted = False