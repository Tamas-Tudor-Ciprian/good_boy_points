# not so simple pygame program


#should have separate functions and clases for event handlling in their own file!

# Import and initialize the pygame library

import player_define

import timing


from block_define import *

from inventory_define import *




# Run until the user asks to quit
running = True



def game():
    pygame.init()


    blocks = [Block(BLOCK_COORD[i]) for i in range(35)]

    blocks.append(Block(BLOCK_COORD[50]))
    blocks.append(Block(BLOCK_COORD[49]))
    blocks.append(Block(BLOCK_COORD[48]))
    blocks.append(Block(BLOCK_COORD[70]))
    blocks.append(Block(BLOCK_COORD[39]))
    blocks.append(Block(BLOCK_COORD[59]))
    blocks.append(Block(BLOCK_COORD[79]))



    running = True

    player = player_define.Player((50,50))
    timer = timing.timer(0.2)

    while running:


        time_delta = timer.delta_timer()
        time_sync = timer.get_timing()


        #make the sky by filling the backround with blue
        SCREEN.fill(SKY_COLOR)

        keys = pygame.key.get_pressed()





        events = pygame.event.get()

        player.update(keys, events, blocks, time_delta, time_sync)


        player.movement()

        player.draw()

        player.hotbar_actions()

        for i in blocks:
            i.draw()

        for event in events:
            if event.type == pygame.QUIT:
                running = False




            # if event.type == pygame.MOUSEBUTTONDOWN:
            #    # pickaxe.mine()
            #     for i in blocks:
            #         if i.block_sprite.collidepoint(event.pos) and comp_dist(player,i,80):
            #             print(event.pos)
            #             print(i)
            #             blocks.remove(i)
            #             del i
            #             break


        # Flip the display
        pygame.display.flip()



    # Done! Time to quit.


    pygame.quit()


game()