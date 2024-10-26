from item_object import *
from sprite_object import *
from math_stuff import *


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
        super().relocate(coord_tuple)
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

    def action(self,events,blocks,player,timing):
        "for some reason if the blocks list is empty you can not place blocks please fix later"

        try_to_place = False
        click_pos = (0,0)


        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                try_to_place = True
                click_pos = event.pos


        if try_to_place and comp_dist_tup(player, click_pos, 200):

            for i in blocks:
                if not i.detector.collidepoint(click_pos):
                    blocks.append(player.inventory.take_item())
                    for j in DETECTOR_RECTANGLES:
                        if j.collidepoint(click_pos):
                            self.relocate((j.x,j.y))
                            break
                    break
