from sprite_object import *
from collision_object import *


class Mob_obj(Game_obj):
    speed = 200

    flicker_nr = 5

    colider_x_offset = 25
    colider_y_offset = 0

    def __init__(self, coord_tuple, sprites_directory,
                 scaling_tuple, health):  # the sprites directory is relative to current file

        #variables pertaining to health and taking damage
        self.health = health
        self.alive = True
        self.took_damage = False

        #why is it so hard to oscilate the state of something at a constant interval
        self.flicker_counter = Mob_obj.flicker_nr
        self.oscillator = True



        #sprite stuff
        super().__init__(coord_tuple)
        self.skin = Sprite_obj(coord_tuple, sprites_directory)
        self.scaling_tuple = scaling_tuple
        self.width = scaling_tuple[0]
        self.height = scaling_tuple[1]

        self.collider = Collision_obj(coord_tuple, scaling_tuple[0] - 50, scaling_tuple[1] - 1)
        self.detector = pygame.Rect(self.x,self.y,scaling_tuple[0],scaling_tuple[1])

        self.left_facing = True
        self.moved_to_side = False

        # these are variables updated every loop
        self.keys = None
        self.events = None
        self.blocks = None
        self.time_delta = None
        self.time_sync = None
        self.mobs = None

        # directional movement functions:
        self.UP = lambda velocity: (self.x, self.y - velocity)
        self.LEFT = lambda velocity: (self.x - velocity, self.y)
        self.RIGHT = lambda velocity: (self.x + velocity, self.y)
        self.DOWN = lambda velocity: (self.x, self.y + velocity)

    def take_damage(self):
        if self.took_damage ==False:
            self.health -= 1
            if self.health <= 0:
                self.alive = False


            self.took_damage = True

    def update(self, keys, events, blocks, mobs, time_delta, time_sync):
        self.keys = keys
        self.events = events
        self.blocks = blocks
        self.mobs = mobs

        # maybe I should just send the whole timer object whole idk
        self.time_delta = time_delta
        self.time_sync = time_sync

    def offset_colider(self, player_coord):
        return (player_coord[0] + Mob_obj.colider_x_offset, player_coord[1] + Mob_obj.colider_y_offset)

    def move(self, velocity, direction):
        new_position = direction(velocity)
        self.relocate(new_position)

        if direction == self.LEFT:
            self.moved_to_side = True
            self.left_facing = True
        elif direction == self.RIGHT:
            self.moved_to_side = True
            self.left_facing = False

    def relocate(self, coord_tuple):
        super().relocate(coord_tuple)
        self.collider.relocate(self.offset_colider(coord_tuple))
        self.skin.relocate(coord_tuple)
        self.detector.x = coord_tuple[0]
        self.detector.y = coord_tuple[1]

    def movement(self):

        velocity = Mob_obj.speed * self.time_delta

        block_rect_list = [i.detector for i in self.blocks]
        mob_rect_list = [i.detector for i in self.mobs]

        block_collisions = self.collider.check(block_rect_list)
        mob_collisions = self.collider.check(mob_rect_list,False)

        # gravity affects all mobs
        if not block_collisions["down"]:
            self.move(velocity * 2, self.DOWN)





        return velocity, block_collisions,mob_collisions

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

        if not self.took_damage:
            self.skin.draw()
        else:
            if self.time_sync:
                if self.oscillator:
                    self.oscillator = False
                else:
                    self.oscillator = True
                    self.flicker_counter -= 1


            if self.oscillator:
                self.skin.draw()

            if self.flicker_counter <= 0:
                self.took_damage = False
                self.flicker_counter = Mob_obj.flicker_nr




        #self.collider.draw()
