from game_object import *
from sprite_object import *
from math_stuff import *
from item_object import *


class Pickaxe(Item_obj):
    """this class will probably help me form the item class"""
    width = 70
    height = 70

    def __init__(self, coord_tuple):
        super().__init__(coord_tuple, r"\pickaxe\pickaxe_sprite", (Pickaxe.width, Pickaxe.height))
        self.mining = False
        self.angle = 0
        self.angular_velocity = 10
        self.block_being_mined = None
        self.mining_position = (0, 0)

    def action(self, events, blocks, player, timing):

        self.block_being_mined = None

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mining = True
                self.mining_position = event.pos



            elif event.type == pygame.MOUSEBUTTONUP:
                self.mining = False

        if self.mining:
            for i in blocks:
                if i.detector.collidepoint(self.mining_position) and comp_dist(player, i, 120):
                    if timing:
                        if i.break_block():
                            player.inventory.add_item(i)
                            blocks.remove(i)
                            break
                    break

    def draw_in_hand(self, hand_coords, left_facing, timing):
        if self.mining and timing:
            self.angle = self.angle + self.angular_velocity
            if left_facing:
                self.in_hand_sprite.rotate(self.angular_velocity)
            else:
                self.in_hand_sprite.rotate(-self.angular_velocity)

        if not self.mining or self.angle >= 30:
            self.in_hand_sprite.change_frame(0)
            self.angle = 0
        hand_coords_to_pass = (hand_coords[0], hand_coords[1] + self.angle)
        super().draw_in_hand(hand_coords_to_pass, left_facing, timing)
