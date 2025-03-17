# not so simple pygame program


# should have separate functions and clases for event handlling in their own file!

# Import and initialize the pygame library


import timing

from block_define import *

from player_define import *
from gremlin_define import *

# Run until the user asks to quit
running = True




def game():

    pygame.init()





    blocks = [Block(BLOCK_COORD[i]) for i in range(31)]

    blocks.append(Block(BLOCK_COORD[50]))
    blocks.append(Block(BLOCK_COORD[49]))
    blocks.append(Block(BLOCK_COORD[48]))
    blocks.append(Block(BLOCK_COORD[70]))
    blocks.append(Block(BLOCK_COORD[39]))
    blocks.append(Block(BLOCK_COORD[59]))
    blocks.append(Block(BLOCK_COORD[79]))

    running = True

    timer = timing.Timer(0.2)


    player = Player((50, 50))
    gremlin = Gremlin((600, 350))

    player_mob_list = []
    gremlin_mob_list = []



    gremlin_mob_list.append(player)
    player_mob_list.append(gremlin)

    while running:

        time_delta = timer.delta_timer()
        time_sync = timer.get_timing()

        # make the sky by filling the backround with blue
        SCREEN.fill(SKY_COLOR)

        keys = pygame.key.get_pressed()

        events = pygame.event.get()



        if player.alive:
            player.update(keys, events, blocks,player_mob_list, time_delta, time_sync)
            player.movement()
            player.draw()
            player.hotbar_actions()
        else:
            gremlin_mob_list.clear()

        if gremlin.alive:
            gremlin.update(keys, events, blocks, gremlin_mob_list, time_delta, time_sync)
            gremlin.movement()
            gremlin.draw()
        else:
            player_mob_list.clear()







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


if __name__ == "__main__":
    game()
