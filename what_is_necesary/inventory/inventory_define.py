import pygame

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
    """there should be some sort of function that say gives the "hand" of the player the sprite of the item 
    to display it <- I wonder if I should make the hand be its own object"""
    def take_item(self):
        temp = self.__item
        self.__item = None
        return temp

    def use_item(self,event,blocks,player):
        if self.__selected and self.__item != None:
            self.__item.action(event,blocks,player) #im not very sure if this will not need any sort of parameters

    def relocate(self,coord_tuple):
        """I don't know if this overloading is really neccessary as
        I don't think I'll be moving the inventory around"""
        super().relocate(coord_tuple)
        self.item_box.relocate(coord_tuple)

    def select_status(self):
        return self.__selected

    def item_status(self):
        return self.__item != None



class Inventory(Game_obj):
    """this"""

    key_select_dict = {
        pygame.K_1 : 0,
        pygame.K_2 : 1,
        pygame.K_3 : 2,
        pygame.K_4 : 3,
        pygame.K_5 : 4,

    }

    collumns = 5

    def __init__(self,coord_tuple):
        super().__init__(coord_tuple)
        #generating these is no easy task
        self.cells = [Inventory_cell((x,self.y)) for x in range(self.x,self.x+Inventory_cell.width*Inventory.collumns,Inventory_cell.width)]
        self.__current_cell = 0
        self.cells[self.__current_cell].select()

    def select_cell(self,keys):
        for key in Inventory.key_select_dict:
            if keys[key]:
                self.cells[self.__current_cell].unselect()
                self.__current_cell = Inventory.key_select_dict[key]
                self.cells[self.__current_cell].select()

    def use_selected_cell(self,event,blocks,player):
        self.cells[self.__current_cell].use_item(event,blocks,player)


    def draw(self,coords,left_facing,timing):
        for i in self.cells:
            i.draw()
            if i.item_status() and i.select_status():
                i.draw_item_in_hand(coords,left_facing,timing)

