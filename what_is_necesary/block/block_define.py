from entity_object import *
from game_constants import *
from sprite_object import *


class Block(Entity_obj):

    def __init__(self,coord_tuple):
        super().__init__(coord_tuple)
        self.detector = pygame.Rect(self.x,self.y,BLOCK_SIDE,BLOCK_SIDE)
        self.sprite = Sprite_obj(coord_tuple,r"\block\block_sprites")
        self.mine_state = [lambda i=i: self.sprite.change_frame(i) for i in range(self.sprite.get_sprite_nr())]
        self.current_mine_state = 0
        self.mine_state[self.current_mine_state]()


    def break_block(self,timing):
        to_return = False
        if timing:
            if self.mine_state[self.current_mine_state] == self.mine_state[-1]:
                to_return = True
            else:
                self.current_mine_state += 1
                self.mine_state[self.current_mine_state]()

        return to_return

    def reset(self):
        self.mine_state[0]()



    def draw(self):
        super().draw()
        self.sprite.scale((BLOCK_SIDE,BLOCK_SIDE))
        self.sprite.draw()
