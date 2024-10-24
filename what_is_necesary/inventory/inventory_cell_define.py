from game_object import *
from sprite_object import *

class Inventory_cell(Game_obj):
    """yeah this one is weird and highly experimental
    it will ultimately be the only type of object allowed to "hold" and item"""

    #I'ma need to define the size ahead apparently

    width = 76
    height = 60

    def __init__(self,coord_tuple):
        super().__init__(coord_tuple)
        #this should be resized according to the width and height using pygame transform
        self.item_box = Sprite_obj(coord_tuple, r"\inventory\inventory_box_sprite")
        self.__item = None
        self.__selected = False


    def select(self):
        self.__selected = True
        self.item_box.change_frame(1)

    def unselect(self):
        self.__selected = False
        self.item_box.change_frame(0)


    def draw(self):
        self.item_box.draw()
        if self.__item != None:
            self.__item.draw()

    def draw_item_in_hand(self,coords,left_facing,timing):
        if self.__item != None:
            self.__item.draw_in_hand(coords,left_facing,timing)

    def add_item(self,item):
        self.__item = item
        self.__item.relocate((self.x,self.y))

    def take_item(self):
        temp = self.__item
        self.__item = None
        return temp

    def use_item(self,event,blocks,player,timing):

        if self.__selected and self.__item != None:
            self.__item.action(event,blocks,player,timing) #im not very sure if this will not need any sort of parameters

    def relocate(self,coord_tuple):
        """I don't know if this overloading is really neccessary as
        I don't think I'll be moving the inventory around"""
        super().relocate(coord_tuple)
        self.item_box.relocate(coord_tuple)

    def select_status(self):
        return self.__selected

    def item_status(self):
        return self.__item != None