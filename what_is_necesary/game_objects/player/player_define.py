from mob_object import *
from pickaxe import *
from health_bar_define import *


class Player(Mob_obj):
    "this having ownership of a sprite_obj might make more sense"

    jump_height = 60


    def __init__(self,coord_tuple):



        super().__init__(coord_tuple,"\\player\\player_sprites",(80,100),3)


        self.health_bar = Health_bar((880,0),self.health)

        self.inventory = Inventory((10,10))
        self.inventory.cells[0].add_item(Pickaxe(self.inventory.cells[0].get_coords()))

        self.last_height = 0
        self.can_jump = False




    def movement(self):

        velocity,block_collisions,mob_collisions = super().movement()




        #this handles the jump and should do so in respect with actual jump height
        #not some arbitrary number that depends on processing speed





        if self.keys[pygame.K_a] and not block_collisions["left"]:
            self.move(velocity,self.LEFT)

        if self.keys[pygame.K_d] and not block_collisions["right"]:
            self.move(velocity,self.RIGHT)

        if (self.keys[pygame.K_SPACE] or self.keys[pygame.K_w]):
            if block_collisions["down"]:
                self.last_height = self.y
                self.can_jump = True
        if self.y > self.last_height - Player.jump_height and not block_collisions["up"] and self.can_jump:
            self.move(velocity * 3,self.UP)
        else:
            self.can_jump = False

        if mob_collisions["left"] or mob_collisions["right"]:
            self.take_damage()
  


    def take_damage(self):
        if not self.took_damage:
            self.health_bar.reduce_health()
        super().take_damage()




    def hotbar_actions(self):

        self.inventory.select_cell(self.keys)
        self.inventory.use_selected_cell(self.events,self.blocks,self,self.time_sync)


    def draw(self):

        super().draw()


        hand_height_offset = 20
        hand_width_offset = 10

        hand_location = (self.x+self.width - hand_width_offset,self.y + self.height/2+hand_height_offset)

        if self.left_facing:
            hand_location = (self.x + hand_width_offset,self.y +self.height /2+hand_height_offset)



        self.inventory.draw(hand_location,self.left_facing,self.time_sync)
        self.health_bar.draw()



