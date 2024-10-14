from sprite_object import *
from game_object import *
from inventory_define import *

class Item_obj(Game_obj):
    """it might make sense to create this class in parralel or at least after the inventory as they ar very interlinked"""



    def __init__(self,coord_tuple,sprite_location,sprite_size = None):
        super().__init__(coord_tuple)
        self.skin = Sprite_obj(coord_tuple,sprite_location)
        self.in_hand_sprite = Sprite_obj(coord_tuple,sprite_location)
        self.sprite_size = sprite_size
        self.right_facing = True




    def action(self):
        pass


    def draw(self):
        self.skin.scale((Inventory_cell.width,Inventory_cell.height))
        self.skin.draw()

    def draw_in_hand(self,coords,left_facing,timing):
        """this function should know how to draw the lower left corner of the sprite always at the location"""
        self.in_hand_sprite.relocate(coords)

        if self.sprite_size != None:
            self.in_hand_sprite.scale(self.sprite_size)

        self.right_facing = not left_facing

        if self.right_facing and self.in_hand_sprite.inverted:
            self.in_hand_sprite.change_frame(0)
        elif not self.right_facing and not self.in_hand_sprite.inverted:
            self.in_hand_sprite.mirror(True, False)

        self.in_hand_sprite.draw()