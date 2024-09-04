import pygame
from defines import *

class Player:



    sprite_display = pygame.display.set_mode((WIDTH,HEIGHT))

    clearance = 10

    speed = 0.2

    width = 80
    height = 100
    right_limit = WIDTH - width
    down_limit = HEIGHT = height

    def __init__(self):
        self.x = 500
        self.y = 200
        self.player_width = 40
        self.player_height = 100
        self.jump_counter = 0
        self.right_limit = WIDTH - self.player_width
        self.down_limit = HEIGHT - self.player_height
        self.character_sprite = pygame.Rect(self.x, self.y, self.player_width, self.player_height)
        self.sprite = pygame.image.load('theGuy_right.png')


    def move_up(self):
        if self.y>0:
            self.y -= Player.speed

    def move_down(self):
        if self.y < self.down_limit:
            self.y += Player.speed
    def move_right(self):
        if self.x < self.right_limit:
            self.x += Player.speed
            self.sprite = pygame.image.load('theGuy_right.png')
    def move_left(self):
        if self.x > 0 :
            self.x -= Player.speed
            self.sprite = pygame.image.load('theGuy_left.png')
    def jump(self,can):
        if can:
            self.jump_counter = 260
        if self.jump_counter > 0:
            self.move_up()
            self.move_up()
            self.move_up()
            self.jump_counter -= 1


    def mine(self):
        pass

    def movement(self,keys,blocks):

        can_jump = False

        down_rect = pygame.Rect(self.x + 2, self.y+self.player_height,self.player_width - 4,1)

        left_rect = pygame.Rect(self.x - 0.2 , self.y, 1, self.player_height)
        right_rect = pygame.Rect(self.x+self.player_width + 0.2, self.y, 1, self.player_height)



        if not any(down_rect.colliderect(i.block_sprite) for i in blocks ):
            self.move_down()
            self.move_down()
        else:
            can_jump = True


        if (keys[pygame.K_w]):
            self.move_up()
            self.move_up()

        if (keys[pygame.K_s]):
            self.move_down()


        if (keys[pygame.K_a]):
            if not any(left_rect.colliderect(i.block_sprite) for i in blocks):
                self.move_left()


        if (keys[pygame.K_d]):
            if not any(right_rect.colliderect(i.block_sprite) for i in blocks):
                self.move_right()


        if (keys[pygame.K_SPACE]):
            self.jump(can_jump)

    def draw(self, screen):
        self.character_sprite = pygame.Rect(self.x, self.y, self.player_width, self.player_height)
        pygame.draw.rect(screen, CHARACTER_COLOR, self.character_sprite)
        Player.sprite_display.blit(self.sprite,(self.x-20,self.y))


