from game_object import *
from game_constants import *


class Collision_obj(Game_obj):
    """the way this object work is by setting up 4 rectangles at a given coordinate and given a list of rectangle objects
    checks collision with each of them to determine the object that is being touched and its direction
    Note: implementing visual cues for debugging purposes might be usefull"""

    rect_thick = 1

    def __init__(self, coord_tuple, width, height):


        self.x = coord_tuple[0]
        self.y = coord_tuple[1]
        super().__init__(coord_tuple)
        self.width = width
        self.height = height

        # here be the "sensor rectangles"
        # you should double check the dimensions and the way you move them around
        # Rect(left, top, width, height) <- this be the declaration

        self.up_rect = pygame.Rect(self.x, self.y - Collision_obj.rect_thick, self.width, Collision_obj.rect_thick)
        self.down_rect = pygame.Rect(self.x, self.y + self.height, self.width, Collision_obj.rect_thick + 1)
        self.left_rect = pygame.Rect(self.x - Collision_obj.rect_thick, self.y, Collision_obj.rect_thick, self.height)
        self.right_rect = pygame.Rect(self.x + self.width, self.y, Collision_obj.rect_thick, self.height)

        # here be what informs the status of the rectangles

    def relocate(self, coord_tuple):
        super().relocate(coord_tuple)
        self.up_rect.x = coord_tuple[0]
        self.up_rect.y = coord_tuple[1] - Collision_obj.rect_thick
        self.right_rect.x = coord_tuple[0] + self.width
        self.right_rect.y = coord_tuple[1]
        self.left_rect.x = coord_tuple[0] - Collision_obj.rect_thick
        self.left_rect.y = coord_tuple[1]
        self.down_rect.x = coord_tuple[0]
        self.down_rect.y = coord_tuple[1] + self.height

    def check(self, to_collide_with,check_for_border = True):

        collision_det = {"up": False, "down": False, "left": False, "right": False}

        if any(self.up_rect.colliderect(i) for i in to_collide_with) or self.up_rect.y <= 0 and check_for_border:
            collision_det["up"] = True
        if any(self.down_rect.colliderect(i) for i in to_collide_with) or self.down_rect.y >= HEIGHT and check_for_border:
            collision_det["down"] = True
        if any(self.left_rect.colliderect(i) for i in to_collide_with) or self.left_rect.x <= 0 and check_for_border:
            collision_det["left"] = True
        if any(self.right_rect.colliderect(i) for i in to_collide_with) or self.right_rect.x >= WIDTH and check_for_border:
            collision_det["right"] = True

        return collision_det

    def draw(self):
        """this function is supposed to draw all 4 rectangles and change their collor when collision is detected"""
        pygame.draw.rect(SCREEN, COLORS["BLACK"], self.up_rect)
        pygame.draw.rect(SCREEN, COLORS["BLACK"], self.left_rect)
        pygame.draw.rect(SCREEN, COLORS["BLACK"], self.right_rect)
        pygame.draw.rect(SCREEN, COLORS["BLACK"], self.down_rect)
