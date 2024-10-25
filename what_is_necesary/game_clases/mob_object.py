from game_object import *
from sprite_object import *
from collision_object import *


class Mob_obj(Game_obj):
    speed = 200

    colider_x_offset = 25
    colider_y_offset = 0

    def __init__(self, coord_tuple, sprites_directory,
                 scaling_tuple):  # the sprites directory is relative to current file

        self.health = 3
        self.alive = True
        self.took_damage = True

        super().__init__(coord_tuple)
        self.skin = Sprite_obj(coord_tuple, sprites_directory)

        self.scaling_tuple = scaling_tuple

        self.width = scaling_tuple[0]
        self.height = scaling_tuple[1]

        self.collider = Collision_obj(coord_tuple, scaling_tuple[0] - 50, scaling_tuple[1] - 1)

        self.left_facing = True
        self.moved_to_side = False

        # these are variables updated every loop
        self.keys = None
        self.events = None
        self.blocks = None
        self.time_delta = None
        self.time_sync = None

        # directional movement functions:
        self.UP = lambda velocity: (self.x, self.y - velocity)
        self.LEFT = lambda velocity: (self.x - velocity, self.y)
        self.RIGHT = lambda velocity: (self.x + velocity, self.y)
        self.DOWN = lambda velocity: (self.x, self.y + velocity)

    def take_damage(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.alive = False
        self.took_damage = True

    def update(self, keys, events, blocks, time_delta, time_sync):
        self.keys = keys
        self.events = events
        self.blocks = blocks

        # maybe I should just send the whole timer object whole idk
        self.time_delta = time_delta
        self.time_sync = time_sync

    def offset_colider(self, player_coord):
        return (player_coord[0] + Mob_obj.colider_x_offset, player_coord[1] + Mob_obj.colider_y_offset)

    def move(self, velocity, direction):
        new_position = direction(velocity)
        self.relocate(new_position)
        self.collider.relocate(self.offset_colider(new_position))
        self.skin.relocate(new_position)
        if direction == self.LEFT:
            self.moved_to_side = True
            self.left_facing = True
        elif direction == self.RIGHT:
            self.moved_to_side = True
            self.left_facing = False

    def movement(self):

        velocity = Mob_obj.speed * self.time_delta

        rect_list = [i.detector for i in self.blocks]

        collisions = self.collider.check(rect_list)

        # gravity affects all mobs
        if not collisions["down"]:
            self.move(velocity * 2, self.DOWN)

        return velocity, collisions

    def draw(self):

        if self.moved_to_side:
            self.skin.animate([1, 2], self.time_sync)
            self.moved_to_side = False
        else:
            self.skin.change_frame(0)

        if self.left_facing and self.skin.inverted:
            self.skin.change_frame(0)
        elif not self.left_facing and not self.skin.inverted:
            self.skin.mirror(True, False)

        self.skin.scale(self.scaling_tuple)
        self.skin.draw()

        self.collider.draw()
