from sprite_object import *



class Health_bar(Game_obj):

    heart_width = 40
    heart_height = 40
    def __init__(self,coord_tuple,heart_amount):
        super().__init__(coord_tuple)
        self.hearts = [Sprite_obj((x, self.y),r"health_bar\heart_sprites") for x in
                      range(self.x, self.x + Health_bar.heart_width * heart_amount,Health_bar.heart_width)]


    def reduce_health(self):
        for i in reversed(self.hearts):
            if i.current_sprite_index !=1:
                i.change_frame(1)
                break

    def draw(self):
        for i in self.hearts:
            i.scale((Health_bar.heart_width,Health_bar.heart_height))
            i.draw()