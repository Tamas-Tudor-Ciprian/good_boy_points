from game_object import *
from game_constants import *
import pygame


class Rect_obj(Game_obj):
    """just realised this class may or may not do absolutely anything special compared to the
    regular pygame rectangle class xD"""
    def __init__(self,coord_tuple,height,width,color,margin_thickness = None,margin_color = None):
        super.__init__(coord_tuple)
        self.margin = margin_thickness
        self.margin_color = margin_color
        self.outer_rectangle = None
        self.color = color
        self.height = height
        self.width = width
        self.rectangle = pygame.Rect(self.x,self.y,self.height,self.width)
        if self.margin != None:
            self.outer_rectangle = pygame.Rect(self.x,self.y,self.height,self.width,self.margin)

    def relocate(self,coord_tuple):
        super().relocate(coord_tuple)
        self.rectangle.x = coord_tuple[0]
        self.rectangle.y = coord_tuple[0]


    def get_rect(self):
        return self.rectangle

    def draw(self,screen):
        pygame.draw.rect(screen,COLORS[self.color],self.rectangle)
        if self.outer_rectangle != None:
            pygame.draw.rect(screen,COLORS[self.margin_color],self.outer_rectangle)
