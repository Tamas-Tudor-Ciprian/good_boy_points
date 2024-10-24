from mob_object import *


class Gremlin(Mob_obj):

    IDLE_TIME = 5
    MOVING_TIME = 20


    def __init__(self,coord_tuple):
        super().__init__(coord_tuple,"\\gremlin\\gremlin_sprites",(100,60))
        self.moving_right = True
        self.stop_counter = Gremlin.MOVING_TIME
        self.to_wait = Gremlin.IDLE_TIME

    def movement(self):
        velocity,collisions = super().movement()

        if collisions["down"] and self.stop_counter > 0:
            if self.moving_right and not collisions["right"]:
                self.move(velocity,self.RIGHT)
            elif  not self.moving_right and not collisions["left"]:
                self.move(velocity,self.LEFT)


        if collisions["right"]:
            self.moving_right = False
        elif collisions["left"]:
            self.moving_right = True

        if self.time_sync:
            self.stop_counter -= 1

        if self.stop_counter <=0 and self.time_sync:
            self.to_wait -= 1

        if self.to_wait <= 0:
            self.stop_counter = Gremlin.MOVING_TIME
            self.to_wait = Gremlin.IDLE_TIME




