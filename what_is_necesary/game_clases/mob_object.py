from game_object import *
from sprite_object import *
from collision_object import *

class Mob_obj(Game_obj):
    speed = 200

    colider_x_offset = 25
    colider_y_offset = 0




    def __init__(self,coord_tuple,sprites_directory): #the sprites directory is relative to current file

        self.health = 3
        self.alive = True

        super().__init__(coord_tuple)
        self.skin = Sprite_obj(coord_tuple,sprites_directory)
        sprite_size = self.skin.get_sprite().get_size()

        self.width = sprite_size[0]
        self.height = sprite_size[1]

        self.collider = Collision_obj(coord_tuple, sprite_size[0] - 50, sprite_size[1] - 1)

        self.left_facing = True
        self.moved_to_side = False

        #these are variables updated every loop
        self.keys = None
        self.events = None
        self.blocks = None
        self.time_delta = None
        self.time_sync = None

        #directional movement functions:
        self.UP = lambda velocity: (self.x, self.y - velocity)
        self.LEFT = lambda velocity: (self.x-velocity,self.y)
        self.RIGHT = lambda velocity: (self.x + velocity,self.y)
        self.DOWN = lambda velocity: (self.x,self.y + velocity)



    def take_damage(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.alive = False


    def update(self,keys,events,blocks,time_delta,time_sync):
        self.keys = keys
        self.events = events
        self.blocks = blocks

        #maybe I should just send the whole timer object whole idk
        self.time_delta = time_delta
        self.time_sync = time_sync

    def offset_colider(self,player_coord):
        return (player_coord[0]+Mob_obj.colider_x_offset,player_coord[1]+Mob_obj.colider_y_offset)



    def move(self,velocity,direction):
        new_position = direction(velocity)
        self.relocate(new_position)
        self.collider.relocate(self.offset_colider(new_position))
        self.skin.relocate(new_position)



    def movement(self):
        pass


    def draw(self):

        if self.moved_to_side:
            self.skin.animate([1,2],self.time_sync)
            self.moved_to_side = False
        else:
            self.skin.change_frame(0)

        if self.left_facing and self.skin.inverted:
            self.skin.change_frame(0)
        elif not self.left_facing and not self.skin.inverted:
            self.skin.mirror(True, False)

        self.skin.draw()