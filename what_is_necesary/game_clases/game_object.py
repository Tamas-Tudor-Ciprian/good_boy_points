
class Game_obj:
    """barebone outline of what a game object will be"""
    def __init__(self,coord_tuple):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]
        self.onscreen = True

    def relocate(self,coord_tuple):
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]

    def get_coords(self):
        return (self.x,self.y)

    def draw(self):
        pass

    def show(self):
        if self.onscreen:
            self.draw()