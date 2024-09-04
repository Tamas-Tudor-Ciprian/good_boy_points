import pygame
from defines import *

class Hotbar:


    slot_height = 50
    slot_width = 50

    slot_nr = 5

    x = WIDTH // 2 - slot_width*slot_nr//2
    y = 20

    def __init__(self):
        self.rect_list = [pygame.Rect(x,Hotbar.y,Hotbar.slot_width,Hotbar.slot_height) for x in range(Hotbar.x,Hotbar.x+Hotbar.slot_width*Hotbar.slot_nr,Hotbar.slot_width)]

    def draw(self,screen):
        for i in self.rect_list:
            pygame.draw.rect(screen, GREY, i, 4)