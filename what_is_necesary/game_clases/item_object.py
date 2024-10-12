from sprite_object import *
from game_object import *

class Item_obj(Game_obj):
    """it might make sense to create this class in parralel or at least after the inventory as they ar very interlinked"""

    def __init__(self,coord_tuple,sprite_location):
        super().__init__(coord_tuple)
        self.skin = Sprite_obj(coord_tuple,sprite_location)


    def action(self):
        pass


    def draw(self):
        self.skin.draw()

    def draw_in_hand(self,coords,left_facing):
        pass