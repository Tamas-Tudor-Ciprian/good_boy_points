from game_object import *
from sprite_object import *


class Inventory_cell(Game_obj):
    """yeah this one is weird and highly experimental
    it will ultimately be the only type of object allowed to "hold" and item"""

    #I'ma need to define the size ahead apparently

    width = 76
    height = 60

    def __init__(self,coord_tuple):
        #this should be resized according to the width and height using pygame transform
        self.item_box = Sprite_obj(coord_tuple, r"\inventory\inventory_box_sprite")
        self.__item = None


    def draw(self):
        self.item_box.draw()
        if self.__item != None:
            self.__item.draw()

    def add_item(self,item):
        self.__item = item
    """there should be some sort of function that say gives the "hand" of the player the sprite of the item 
    to display it <- I wonder if I should make the hand be its own object"""
    def take_item(self):
        temp = self.__item
        self.__item = None
        return temp

    def use_item(self):
        self.__item.action() #im not very sure if this will not need any sort of parameters

    def relocate(self,coord_tuple):
        """I don't know if this overloading is really neccessary as
        I don't think I'll be moving the inventory around"""
        super().relocate(coord_tuple)
        self.item_box.relocate(coord_tuple)



class Inventory(Game_obj):
    """this"""
    def __init__(self,coord_tuple,collumns):
        super().__init__(coord_tuple)
        #generating these is no easy task
        self.cells = [Inventory_cell((x,self.y)) for x in range(self.x,self.x+Inventory_cell.width*collumns,Inventory_cell.width)]



    def draw(self):
        for i in self.cells:
            i.draw()