from game_object import *
import pygame
from game_constants import *
class Collision_obj(Game_obj):
    """the way this object work is by setting up 4 rectangles at a given coordinate and given a list of rectangle objects
    checks collision with each of them to determine the object that is being touched and its direction"""
    def __init__(self,coord_tuple,width,height):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]
        super().__init__(coord_tuple)
        self.width = width
        self.height = height

        # here be the "sensor rectangles"
        self.rectangle_up = pygame.Rect(self.x, self.y, self.height, self.width)
        self.rectangle_right = pygame.Rect(self.x, self.y, self.height, self.width)
        self.rectangle_left = pygame.Rect(self.x, self.y, self.height, self.width)
        self.rectangle_down = pygame.Rect(self.x, self.y, self.height, self.width)
        self.up_rect = pygame.Rect(self.x + self.width, self.y -2, self.width - 4, 1)
        self.down_rect = pygame.Rect(self.x + 2, self.y + self.height, self.width - 4, 1)
        self.left_rect = pygame.Rect(self.x - 0.2, self.y, 1, self.height)
        self.right_rect = pygame.Rect(self.x + self.width + 0.2, self.y, 1, self.height)


        #here be what informs the status of the rectangles

    def check(self,to_collide_with):

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