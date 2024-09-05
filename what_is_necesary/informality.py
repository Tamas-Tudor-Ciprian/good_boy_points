# Simple pygame program

# Import and initialize the pygame library
import pygame
import player_define
import hotbar_define
import time
import item_define

from defines import *
from block_define import *



# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Run until the user asks to quit
running = True


def game():
    pygame.init()







    block_coord = tuple((i, j)for j in range(450, -50, -50) for i in range(0, 1000, 50) )

    player = player_define.Player()
    pickaxe = item_define.Pickaxe(player.player_coords(),(55,35),'pickaxe.png',)
    hotbar = hotbar_define.Hotbar()




    blocks = [Block(block_coord[i]) for i in range(35)]

    blocks.append(Block(block_coord[50]))
    blocks.append(Block(block_coord[49]))
    blocks.append(Block(block_coord[48]))
    blocks.append(Block(block_coord[70]))
    blocks.append(Block(block_coord[39]))
    blocks.append(Block(block_coord[59]))
    blocks.append(Block(block_coord[79]))


    running = True

    last_time = time.time()

    while running:



        curent_time = time.time()

        time_delta = curent_time - last_time

        last_time = curent_time

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #make the sky by filling the backround with blue
        screen.fill(SKY_COLOR)

        pickaxe.set_coords(player.player_coords())

        keys = pygame.key.get_pressed()



        player.movement(keys,blocks)

        pickaxe.draw()

        pickaxe.mine()

        player.draw(screen)
        hotbar.draw(screen)






        for i in blocks:
            i.draw(screen)

        # Flip the display
        pygame.display.flip()



    # Done! Time to quit.



    pygame.quit()



game()