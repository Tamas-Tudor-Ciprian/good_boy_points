from sprite_object import *
from game_object import *
from inventory_define import *

class Item_obj(Game_obj):
    """it might make sense to create this class in parralel or at least after the inventory as they ar very interlinked"""

    def __init__(self,coord_tuple,sprite_location,sprite_size = None):
        super().__init__(coord_tuple)
        self.skin = Sprite_obj(coord_tuple,sprite_location)


    def action(self):
        pass


    def draw(self):
        self.skin.scale((Inventory_cell.width,Inventory_cell.height))
        self.skin.draw()

    def draw_in_hand(self,coords,left_facing):
        pass