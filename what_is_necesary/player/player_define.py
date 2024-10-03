
from game_object import *
from collision_object import *
from sprite_object import *
from item_object import *
import os

class Player(Sprite_obj):
    "this may be more efficient by also inheriting the collision object instead of having ownership of one"
    speed = 200
    jump_height = 100
    sprites_location = os.getcwd() + "\\player\\player_sprites"

    def __init__(self,coord_tuple):
        super().__init__(coord_tuple,Player.sprites_location)
        sprite_size = self.get_default_sprite().get_size()
        self.collider = Collision_obj(coord_tuple,sprite_size[0],sprite_size[1])
        in_hand = Item_obj()
        self.jump_counter = Player.jump_height

    def move_up(self,time_delta):
        new_position = (self.x,self.y-Player.speed*time_delta)
        self.relocate(new_position)
        self.collider.relocate(new_position)
    def move_left(self,time_delta):
        new_position = (self.x-Player.speed*time_delta,self.y)
        self.relocate(new_position)
        self.collider.relocate(new_position)
    def move_right(self,time_delta):
        new_position = (self.x + Player.speed*time_delta,self.y)
        self.relocate(new_position)
        self.collider.relocate(new_position)
    def move_down(self,time_delta):
        new_position = (self.x,self.y + Player.speed*time_delta)
        self.relocate(new_position)
        self.collider.relocate(new_position)



    def movement(self,keys,rectangle_list,time_delta):

        velocity = self.speed * time_delta
        collisions = self.collider.check(rectangle_list)

        if not collisions["down"]:
           self.move_down(time_delta)

        if keys[pygame.K_a] and collisions["left"]:
            self.move_left(time_delta)

        if keys[pygame.K_d] and collisions["right"]:
            self.move_right(time_delta)

        if (keys[pygame.K_SPACE] or keys[pygame.K_w]):
            self.move_up(time_delta)
            self.move_up(time_delta)
            self.jump_counter -= 1
            if self.jump_counter == 0 and collisions["down"]:
                self.jump_counter = Player.jump_height

    def in_hand_action(self,activated):
        pass