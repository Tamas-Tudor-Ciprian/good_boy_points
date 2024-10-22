import pygame

from game_object import *
from sprite_object import *
from inventory_cell_define import *





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

    def use_selected_cell(self,event,blocks,player,timing):

        self.cells[self.__current_cell].use_item(event,blocks,player,timing)

    def add_item(self,item):
        for cell in self.cells:
            if  not cell.item_status():
                cell.add_item(item)
                break

    def take_item(self):
        return self.cells[self.__current_cell].take_item()

    def draw(self,coords,left_facing,timing):
        for i in self.cells:
            i.draw()
            if i.item_status() and i.select_status():
                i.draw_item_in_hand(coords,left_facing,timing)