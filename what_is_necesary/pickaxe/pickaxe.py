from game_object import *
from sprite_object import *
from math_stuff import *
from item_object import *

class Pickaxe(Item_obj):
    """this class will probably help me form the item class"""
    def __init__(self,coord_tuple):
        super().__init__(coord_tuple,r"\pickaxe\pickaxe_sprite",)

    def action(self,event,blocks,player):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # pickaxe.mine()
            for i in blocks:
                if i.block_sprite.collidepoint(event.pos) and comp_dist(player, i, 80):
                    print(event.pos)
                    print(i)
                    blocks.remove(i)
                    del i
                    break