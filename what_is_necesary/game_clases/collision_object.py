from game_object import *
import pygame
from game_constants import *
class Collision_obj(Game_obj):
    """the way this object work is by setting up 4 rectangles at a given coordinate and given a list of rectangle objects
    checks collision with each of them to determine the object that is being touched and its direction
    Note: implementing visual cues for debugging purposes might be usefull"""
    def __init__(self,coord_tuple,width,height):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]
        super().__init__(coord_tuple)
        self.width = width
        self.height = height

        # here be the "sensor rectangles"
        #you should double check the dimensions and the way you move them around

        self.up_rect = pygame.Rect(self.x + self.width, self.y -2, self.width - 4, 1)
        self.down_rect = pygame.Rect(self.x + 2, self.y + self.height, self.width - 4, 1)
        self.left_rect = pygame.Rect(self.x - 0.2, self.y, 1, self.height)
        self.right_rect = pygame.Rect(self.x + self.width + 0.2, self.y, 1, self.height)


        #here be what informs the status of the rectangles

    def relocate(self,coord_tuple):
        super().relocate(coord_tuple)
        self.up_rect.x = coord_tuple[0]
        self.up_rect.y = coord_tuple[1]
        self.right_rect.x = coord_tuple[0]
        self.right_rect.y = coord_tuple[1]
        self.left_rect.x = coord_tuple[0]
        self.left_rect.y = coord_tuple[1]
        self.down_rect.x = coord_tuple[0]
        self.down_rect.y = coord_tuple[1]


    def check(self,to_collide_with):

        collision_det = {"up":False,"down":False,"left":False,"right":False}

        if any(self.up_rect.colliderect(i) for i in to_collide_with) or self.up_rect.y <= 0:
            collision_det["up"] = True
        if any(self.up_rect.colliderect(i) for i in to_collide_with) or self.down_rect.y >= HEIGHT:
            collision_det["down"] = True
        if any(self.up_rect.colliderect(i) for i in to_collide_with) or self.left_rect.x <= 0:
            collision_det["left"] = True
        if any(self.up_rect.colliderect(i) for i in to_collide_with) or self.right_rect.x >= WIDTH:
            collision_det["right"] = True


        return collision_det

    def draw(self,screen):
        """this function is supposed to draw all 4 rectangles and change their collor when collision is detected"""
        pygame.draw.rect(screen,COLORS["GREEN"],self.up_rect)
        pygame.draw.rect(screen, COLORS["GREEN"], self.left_rect)
        pygame.draw.rect(screen, COLORS["GREEN"], self.right_rect)
        pygame.draw.rect(screen, COLORS["GREEN"], self.down_rect)