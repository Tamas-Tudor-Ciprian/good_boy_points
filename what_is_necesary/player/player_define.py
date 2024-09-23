
from game_object import *
from collision_object import *
from sprite_object import *
from item_object import *
class Player(Game_obj):
    def __init__(self,coord_tuple):
        super(coord_tuple)
        self.sprite = Sprite_obj(coord_tuple)
        self.collider = Collision_obj(coord_tuple)
        self.velocity = 1
        in_hand = Item_obj()

    def move_up(self,time_delta):
        pass
    def move_left(self,time_delta):
        pass
    def move_right(self,time_delta):
        pass
    def move_down(self,time_delta):
        pass

    def movement(self,keys,rectangle_list,time_delta):
        collisions = self.collider.check(rectangle_list)



    def in_hand_action(self):
        pass
    def draw(self):
        pass

    def run_functionality(self):
        pass

