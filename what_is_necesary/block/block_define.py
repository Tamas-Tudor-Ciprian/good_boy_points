from item_object import *
from game_constants import *
from sprite_object import *


class Block(Item_obj):

    def __init__(self,coord_tuple):
        super().__init__(coord_tuple,r"\block\block_sprites")
        self.detector = pygame.Rect(self.x,self.y,BLOCK_SIDE,BLOCK_SIDE)
        self.sprite = Sprite_obj(coord_tuple,r"\block\block_sprites")
        self.mine_state = [lambda i=i: self.sprite.change_frame(i) for i in range(self.sprite.get_sprite_nr())]
        self.current_mine_state = 0
        self.mine_state[self.current_mine_state]()


    def break_block(self):
        to_return = False
        if self.current_mine_state == len(self.mine_state) - 1:
            to_return = True
        else:
            self.current_mine_state += 1
            self.mine_state[self.current_mine_state]()

        return to_return

    def reset(self):
        self.mine_state[0]()

    def relocate(self,coord_tuple):
        self.detector.x = coord_tuple[0]
        self.detector.y = coord_tuple[1]

        self.sprite.x = coord_tuple[0]
        self.sprite.y = coord_tuple[1]

        self.sprite.change_frame(0)
        self.current_mine_state = 0

    def draw(self):
        self.sprite.scale((BLOCK_SIDE,BLOCK_SIDE))
        self.sprite.draw()
        pygame.draw.rect(SCREEN,BLACK,self.detector,1)

    def action(self,event,blocks,player,timing):
        pass
