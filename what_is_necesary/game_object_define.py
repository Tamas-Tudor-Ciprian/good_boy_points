
#new code standard: if I use a class that I did not make myself then that class will not be
#a parent class for any of my clases, my framework and the imported framework stay separate

import pygame
from defines import *



class Game_obj:
    """barebone outline of what a game object will be"""
    def __init__(self,coord_tuple):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]

    def relocate(self,coord_tuple):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]


class Sprite_obj(Game_obj):
    """this class takes care of putting the sprite on the screen and animating it when needed"""
    sprite_display = pygame.display.set_mode((WIDTH,HEIGHT))
    def __init__(self,coord_tuple,sprites_paths):
        super.__init__(coord_tuple)
        self.sprites =[pygame.image.load(i) for i in sprites_paths]
        self.frame = 0

    def draw(self):
        Sprite_obj.sprite_display.blit(self.sprites[self.frame],(self.x,self.y))


    def animate(self,frames,timing):
        if self.frame in frames:
            i = frames.index(self.frame)
            if self.frame != frames[-1]:
                self.frame = frames(i+1)
            else:
                self.frame = frames[0]
        else:
            self.frame = frames[0]


class Rect_obj(Game_obj):
    """just realised this class may or may not do absolutely anything special compared to the
    regular pygame rectangle class xD
    -note to self : add actual margins with their own colors"""
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

    def draw(self,screen):
        pygame.draw.rect(screen,COLORS[self.color],self.rectangle)
        if self.outer_rectangle != None:
            pygame.draw.rect(screen,COLORS[self.margin_color],self.outer_rectangle)


class Collision_obj(Game_obj):
    """the way this object work is by setting up 4 rectangles at a given coordinate and given a list of rectangle objects
    checks collision with each of them to determine the object that is being touched and its direction"""
    def __init__(self,coord_tuple,width,height):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]
        self.width = width
        self.height = height

        # here be the "sensor rectangles"
        self.rectangle_up = pygame.Rect(self.x, self.y, self.height, self.width)
        self.rectangle_right = pygame.Rect(self.x, self.y, self.height, self.width)
        self.rectangle_left = pygame.Rect(self.x, self.y, self.height, self.width)
        self.rectangle_down = pygame.Rect(self.x, self.y, self.height, self.width)




