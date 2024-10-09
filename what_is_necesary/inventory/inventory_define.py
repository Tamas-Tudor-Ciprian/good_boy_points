from game_object import *
from sprite_object import *


class Inventory_cell(Game_obj):
    """yeah this one is weird and highly experimental
    it will ultimately be the only type of object allowed to "hold" and item"""
    def __init__(self,coord_tuple):

        self.item_box = Sprite_obj(coord_tuple,r"\inventory\inventory_box_sprite")
        self.__item = None


    def draw(self):
        self.item_box.draw()
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




class Inventory(Game_obj):
    """this"""
    def __init__(self,coord_tuple,collumns):
        super().__init__(coord_tuple)
        #generating theese is no easy task
        self.cells = [Inventory_cell((x,self.y) for x in range(self.x,self.x*collumns,Inventory_cell.))]



    def draw(self):
        pass