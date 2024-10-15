from game_object import *
from sprite_object import *
from math_stuff import *
from item_object import *

class Pickaxe(Item_obj):
    """this class will probably help me form the item class"""
    def __init__(self,coord_tuple):
        super().__init__(coord_tuple,r"\pickaxe\pickaxe_sprite",(70,70))
        self.rotating = False


    def action(self,event,blocks,player):
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.in_hand_sprite.rotate(10)
            for i in blocks:
                if i.block_sprite.collidepoint(event.pos) and comp_dist(player, i, 80):
                    blocks.remove(i)
                    del i
                    break