from inventory_define import *

class Item_obj(Game_obj):
    """it might make sense to create this class in parralel or at least after the inventory as they ar very interlinked"""



    def __init__(self,coord_tuple,sprite_location,sprite_size = None):
        super().__init__(coord_tuple)
        self.skin = Sprite_obj(coord_tuple,sprite_location)
        self.in_hand_sprite = Sprite_obj(coord_tuple,sprite_location)
        self.sprite_size = sprite_size
        self.right_facing = True

        if sprite_size != None:
            self.width = sprite_size[0]
            self.height = sprite_size[1]
        else:
            self.width = self.skin.get_sprite().get_width()
            self.height = self.skin.get_sprite().get_height()



    def action(self):
        pass


    def draw(self):
        self.skin.scale((Inventory_cell.width,Inventory_cell.height))
        self.skin.draw()

    def draw_in_hand(self,hand_coords,left_facing,timing):
        """this function should know how to draw the lower left corner of the sprite always at the location"""

        self.right_facing = not left_facing

        #this is so that the corner is always in the hand
        shifted_coords = (hand_coords[0],hand_coords[1]-self.height)
        if not self.right_facing:
            shifted_coords = (hand_coords[0]-self.width,hand_coords[1]-self.height)

        self.in_hand_sprite.relocate(shifted_coords)

        if self.sprite_size != None:
            self.in_hand_sprite.scale(self.sprite_size)



        if self.right_facing and self.in_hand_sprite.inverted:
            self.in_hand_sprite.change_frame(0)
        elif not self.right_facing and not self.in_hand_sprite.inverted:
            self.in_hand_sprite.mirror(True, False)

        self.in_hand_sprite.draw()