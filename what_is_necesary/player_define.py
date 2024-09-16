import pygame
from defines import *


#this is way to long optimisation and splitting needed, rework this!

class Player:

    """this class needs to be completly revamped"""


    sprite_display = pygame.display.set_mode((WIDTH,HEIGHT))

    clearance = 10




    speed = 250

    width = 80
    height = 100
    right_limit = WIDTH - width
    down_limit = HEIGHT - height

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
        self.sprite_frame = 0
        self.can_jump = False
        self.face_right = True
        self.foot_up = False
        self.velocity = Player.speed

    def move_up(self):
        if self.y>0:
            self.y -= self.velocity

    def move_down(self):
        if self.y < self.down_limit:
            self.y += self.velocity
    def move_right(self):
        self.face_right = True
        if self.x < self.right_limit:
            self.x += self.velocity

            if self.foot_up == False:
                self.sprite_frame = 2
                self.foot_up = True
            else:
                self.sprite_frame = 3
                self.foot_up = False

            if self.can_jump == False:
                self.sprite_frame = 0

    def move_left(self):
        self.face_right = False
        if self.x > 0:
            self.x -= self.velocity

            if self.foot_up == False:
                self.sprite_frame = 4
                self.foot_up = True
            else:
                self.sprite_frame = 5
                self.foot_up = False
            if self.can_jump == False:
                self.sprite_frame = 1




    def jump(self):
        if self.can_jump:
            self.jump_counter = 260
        if self.jump_counter > 0:
            self.move_up()
            self.move_up()
            self.move_up()
            self.jump_counter -= 1



    def movement(self,keys,blocks,time_delta):

        self.velocity = Player.speed * time_delta

        if self.face_right == True:
            self.sprite_frame = 0
        else:
            self.sprite_frame = 1

        self.can_jump = False

        down_rect = pygame.Rect(self.x + 2, self.y+self.player_height,self.player_width - 4,1)

        left_rect = pygame.Rect(self.x - 0.2 , self.y, 1, self.player_height)
        right_rect = pygame.Rect(self.x+self.player_width + 0.2, self.y, 1, self.player_height)



        if not any(down_rect.colliderect(i.block_sprite) for i in blocks ):
            self.move_down()
            self.move_down()
        else:
            self.can_jump = True


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
            self.jump()

        return self.face_right



    def player_coords(self):
        return (self.x,self.y)
    def draw(self, screen):
        self.character_sprite = pygame.Rect(self.x, self.y, self.player_width, self.player_height)
        pygame.draw.rect(screen, CHARACTER_COLOR, self.character_sprite)
        Player.sprite_display.blit(self.sprite,(self.x-20,self.y))

        if self.sprite_frame == 0:
            self.sprite = pygame.image.load('theGuy_right.png')
        elif self.sprite_frame == 1:
            self.sprite = pygame.image.load('theGuy_left.png')
        elif self.sprite_frame == 2:
            self.sprite = pygame.image.load('theGuy_right_rightFoot.png')
        elif self.sprite_frame == 3:
            self.sprite = pygame.image.load('theGuy_right_leftFoot.png')
        elif self.sprite_frame == 4:
            self.sprite = pygame.image.load('theGuy_left_leftFoot.png')
        elif self.sprite_frame == 5:
            self.sprite = pygame.image.load('theGuy_left_rightFoot.png')


