
#new code standard: if I use a class that I did not make myself then that class will not be
#a parent class for any of my clases, my framework and the imported framework stay separate

import pygame
from defines import *



class Game_obj:
    """barebone outline of what a game object will be"""
    def __init__(self,coord_tuple):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]
        self.onscreen = True

    def relocate(self,coord_tuple):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]

    def get_coords(self):
        return (self.x,self.y)

    def draw(self):
        pass

    def show(self):
        if self.onscreen:
            self.draw()

class Sprite_obj(Game_obj):
    """this class takes care of putting the sprite on the screen and animating it when needed"""
    sprite_display = pygame.display.set_mode((WIDTH,HEIGHT))
    def __init__(self,coord_tuple,sprites_paths):
        super.__init__(coord_tuple)
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


class Collision_obj(Game_obj):
    """the way this object work is by setting up 4 rectangles at a given coordinate and given a list of rectangle objects
    checks collision with each of them to determine the object that is being touched and its direction"""
    def __init__(self,coord_tuple,width,height):
        super(coord_tuple)
        self.width = width
        self.height = height

        # here be the "sensor rectangles"
        self.up_rect = pygame.Rect(self.x + self.width, self.y -2, self.width - 4, 1)
        self.down_rect = pygame.Rect(self.x + 2, self.y + self.height, self.width - 4, 1)
        self.left_rect = pygame.Rect(self.x - 0.2, self.y, 1, self.height)
        self.right_rect = pygame.Rect(self.x + self.width + 0.2, self.y, 1, self.height)


        #here be what informs the status of the rectangles



    def check_collision(self,to_collide_with):

        collision_det = {"up":False,"down":False,"left":False,"right":False}

        if any(self.up_rect.colliderect(i.block_sprite) for i in to_collide_with) or self.up_rect.y <= 0:
            collision_det["up"] = True
        if any(self.up_rect.colliderect(i.block_sprite) for i in to_collide_with) or self.up_rect.y >= HEIGHT:
            collision_det["down"] = True
        if any(self.up_rect.colliderect(i.block_sprite) for i in to_collide_with) or self.up_rect.x <= 0:
            collision_det["left"] = True
        if any(self.up_rect.colliderect(i.block_sprite) for i in to_collide_with) or self.up_rect.x >= WIDTH:
            collision_det["right"] = True


        return collision_det


class Sprite_rect_obj(Sprite_obj,Rect_obj):
    """this class will be used to revamp the block_define"""
    pass

class Item_sprite_obj(Sprite_obj):
    pass