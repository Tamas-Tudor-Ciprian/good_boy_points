from mob_object import *


class Gremlin(Mob_obj):

    IDLE_TIME = 5
    MOVING_TIME = 20


    def __init__(self,coord_tuple):
        super().__init__(coord_tuple,"\\gremlin\\gremlin_sprites",(100,60),1)
        self.moving_right = True
        self.stop_counter = Gremlin.MOVING_TIME
        self.to_wait = Gremlin.IDLE_TIME

    def movement(self):
        velocity,block_collisions,mob_collisions = super().movement()

        if block_collisions["down"] and self.stop_counter > 0:
            if self.moving_right and not block_collisions["right"]:
                self.move(velocity,self.RIGHT)
            elif  not self.moving_right and not block_collisions["left"]:
                self.move(velocity,self.LEFT)


        if block_collisions["right"]:
            self.moving_right = False
        elif block_collisions["left"]:
            self.moving_right = True

        if self.time_sync:
            self.stop_counter -= 1

        if self.stop_counter <=0 and self.time_sync:
            self.to_wait -= 1

        if self.to_wait <= 0:
            self.stop_counter = Gremlin.MOVING_TIME
            self.to_wait = Gremlin.IDLE_TIME

        if mob_collisions["up"] and not mob_collisions["left"] and not mob_collisions["right"]:
            self.take_damage()





