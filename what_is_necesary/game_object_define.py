import pygame
from defines import *



class Game_obj:

    def __init__(self,x,y):
        self.x = x
        self.y = y



class Sprite_obj(Game_obj):

    sprite_display = pygame.display.set_mode((WIDTH,HEIGHT))
    def __init__(self,x,y,sprites_paths):
        super.__init__(x,y)
        self.sprites =[pygame.image.load(i) for i in sprites_paths]
        self.frame = 0

    def draw(self):
        Sprite_obj.sprite_display.blit(self.sprites[self.frame],(self.x,self.y))
class Rect_obj:
    pass

class Rect_sprite_obj:
    pass



class collision_obj:
    pass