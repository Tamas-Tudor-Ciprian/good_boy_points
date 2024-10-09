
from game_object import *
from collision_object import *
from sprite_object import *
from item_object import *
from game_object import *
import os

class Player(Game_obj):
    "this having ownership of a sprite_obj might make more sense"
    speed = 200
    jump_height = 310


    colider_x_offset = 25
    colider_y_offset = 0

    def __init__(self,coord_tuple):
        super().__init__(coord_tuple)
        self.skin = Sprite_obj(coord_tuple,"\\player\\player_sprites")
        sprite_size = self.skin.get_sprite().get_size()
        self.collider = Collision_obj(coord_tuple,sprite_size[0]-50,sprite_size[1])
        self.jump_counter = 0
        self.left_facing = True
        self.moved_to_side = False

    def offset_colider(self,player_coord):
        return (player_coord[0]+Player.colider_x_offset,player_coord[1]+Player.colider_y_offset)

    def move_up(self,velocity):
        new_position = (self.x,self.y-velocity)
        self.relocate(new_position)
        self.collider.relocate(self.offset_colider(new_position))
        self.skin.relocate(new_position)
    def move_left(self,velocity):

        new_position = (self.x-velocity,self.y)
        self.relocate(new_position)
        self.collider.relocate(self.offset_colider(new_position))
        self.skin.relocate(new_position)

        self.moved_to_side = True
        self.left_facing = True
    def move_right(self,velocity):

        new_position = (self.x + velocity,self.y)
        self.relocate(new_position)
        self.collider.relocate(self.offset_colider(new_position))
        self.skin.relocate(new_position)


        self.moved_to_side = True
        self.left_facing = False
    def move_down(self,velocity):
        new_position = (self.x,self.y + velocity)
        self.relocate(new_position)
        self.collider.relocate(self.offset_colider(new_position))
        self.skin.relocate(new_position)



    def movement(self,keys,rectangle_list,time_delta):

        velocity = self.speed * time_delta
        collisions = self.collider.check(rectangle_list)





        if not collisions["down"]:
           self.move_down(velocity *2)

        if keys[pygame.K_a] and not collisions["left"]:
            self.move_left(velocity)

        if keys[pygame.K_d] and not collisions["right"]:
            self.move_right(velocity)

        if (keys[pygame.K_SPACE] or keys[pygame.K_w]):
            if self.jump_counter > 0 :
                self.move_up(velocity*3)
                self.jump_counter -= 1
            if self.jump_counter == 0 and collisions["down"]:
                self.jump_counter = Player.jump_height


    def draw(self,screen,timing):


        if self.moved_to_side:
            self.skin.animate([1,2],timing)
            self.moved_to_side = False
        else:
            self.skin.change_frame(0)


        if self.left_facing and self.skin.inverted:
            self.skin.change_frame(0)
        elif not self.left_facing and not self.skin.inverted:
            self.skin.mirror(True, False)



        self.skin.draw()

        #self.collider.draw(screen)

    def in_hand_action(self,activated):
        pass