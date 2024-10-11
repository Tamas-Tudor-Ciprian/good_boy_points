from game_object import *
from sprite_object import *
from math_stuff import *


class Pickaxe(Game_obj):
    def __init__(self,coord_tuple):
        super().__init__(coord_tuple)
        self.skin = Sprite_obj(coord_tuple,r"\pickaxe")



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