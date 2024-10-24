from mob_object import *


class Gremlin(Mob_obj):



    def __init__(self,coord_tuple):
        super().__init__(coord_tuple,"\\gremlin\\gremlin_sprites",(100,60))

    def movement(self):
        velocity,collisions = super().movement()