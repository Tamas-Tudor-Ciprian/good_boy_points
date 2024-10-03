
from game_object import *
from collision_object import *
from sprite_object import *
from item_object import *
import os

class Player(Sprite_obj):
    "this having ownership of a sprite_obj might make more sense"
    speed = 200
    jump_height = 100
    sprites_location = os.getcwd() + "\\player\\player_sprites"

    def __init__(self,coord_tuple):
        super().__init__(coord_tuple,Player.sprites_location)
        sprite_size = self.get_default_sprite().get_size()
        self.collider = Collision_obj(coord_tuple,sprite_size[0],sprite_size[1])
        in_hand = Item_obj()
        self.jump_counter = Player.jump_height

    def move_up(self,velocity):
        new_position = (self.x,self.y-velocity)
        self.relocate(new_position)
        self.collider.relocate(new_position)
    def move_left(self,velocity):
        new_position = (self.x-velocity,self.y)
        self.relocate(new_position)
        self.collider.relocate(new_position)
    def move_right(self,velocity):
        new_position = (self.x + velocity,self.y)
        self.relocate(new_position)
        self.collider.relocate(new_position)
    def move_down(self,velocity):
        new_position = (self.x,self.y + velocity)
        self.relocate(new_position)
        self.collider.relocate(new_position)



    def movement(self,keys,rectangle_list,time_delta):

        velocity = self.speed * time_delta
        collisions = self.collider.check(rectangle_list)

        if not collisions["down"]:
           self.move_down(velocity)

        if keys[pygame.K_a] and not collisions["left"]:
            self.move_left(velocity)

        if keys[pygame.K_d] and not collisions["right"]:
            self.move_right(velocity)

        if (keys[pygame.K_SPACE] or keys[pygame.K_w]):
            if self.jump_counter >= 0 :
                self.move_up(velocity)
                self.move_up(velocity)
                self.jump_counter -= 1
            if self.jump_counter == 0 and collisions["down"]:
                self.jump_counter = Player.jump_height


    def draw(self,screen):
        self.collider.draw(screen)
        super().draw()

    def in_hand_action(self,activated):
        pass