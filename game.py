import pygame
import random
import matplotlib.pyplot as plt

from game_helpers import *
from basic_strats import rand_strat, player_strat

def run_game(screen, player1,  player2): # provide the two strategy functions
    frame_limit = 10000

    strat1, strat1_name = player1
    strat2, strat2_name = player1
    game_state = [[0]*7 for i in range(6)] # generate empty board
    result = 0
    turn = 1
    
    # pygame iniialisation
    clock = pygame.time.Clock()

    bg_color = (0, 0x23, 0x28)
    screen.fill(bg_color)

    # Player Names
    font = pygame.font.Font(None, 50)
    fontLarge = pygame.font.Font(None, 80)

    # Names Canvas
    player_names = pygame.Surface((700, 300), pygame.SRCALPHA)
    player_rect = player_names.get_rect(topleft = (0, 0))

    # Player 1 Canvas
    player1 = font.render(strat1_name, True, (0xde, 0x04, 0x04))
    player1_rect = player1.get_rect(topleft = (20, 20))
    
    # Player 2 Canvas
    player2 = font.render(strat2_name, True, (0xe2, 0xd7, 0x0c))
    player2_rect = player1.get_rect(topright = (680, 20))

    # Placing names on Names Canvas
    player_names.blit(player1, player1_rect)
    player_names.blit(player2, player2_rect)

    board_sprite = pygame.Surface((700, 600), pygame.SRCALPHA) # create board with background
    board_rect = board_sprite.get_rect(topleft = (0, 300))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        move_list = [] # generate move list
        if turn != 0:
            for j in range(len(game_state[0])):
                for i in range(len(game_state)-1, -1, -1):
                    if game_state[i][j] == 0:
                        move_list.append((i, j))
                        break

        draw_board(screen, player_names, player_rect, board_sprite, board_rect, game_state) # show base screen
        pygame.display.update()
        
        animation_speed = 600 # controls ball fall speed - recommended : 4
        if len(move_list): # if there are moves left to make, pass game to strategy functions
            if turn == 1:
                i, j = strat1(game_state, move_list) # determine move
                for r in range(100, 350 + 100 * i, animation_speed): # animate ball falling
                    draw_board(screen, player_names, player_rect, board_sprite, board_rect, game_state, (50 + 100*j, r), turn)
                    pygame.display.update() # update screen to show animation step
                game_state[i][j] = turn

            elif turn == 2:
                i, j = strat2(game_state, move_list) # determine move
                for r in range(100, 350 + 100 * i, animation_speed): # animate ball falling
                    draw_board(screen, player_names, player_rect, board_sprite, board_rect, game_state, (50 + 100*j, r), turn)
                    pygame.display.update() # update screen to show animation step
                game_state[i][j] = turn

            # if check_win_visual(clock, screen, player_names, player_rect, board_sprite, board_rect, game_state, turn):
            if check_win(game_state, turn): # Game Won?
                print(f"Last Move: {turn} - {i}, {j}")
        
                # Show Winner Name in their Colour
                winner_name = fontLarge.render(strat1_name if turn == 1 else strat2_name, True, (0xde, 0x04, 0x04) if turn == 1 else (0xe2, 0xd7, 0x0c)) 
                winner_rect = winner_name.get_rect(center = (350, 150))
                player_names.blit(winner_name, winner_rect)

                result = turn
                turn = 0
            else:
                turn = 3 - turn

        elif turn != 0:
            # Game Draw - Show Text
            gamedraw = fontLarge.render("Draw", True, (0xff, 0xff, 0xff))
            gamedraw_rect = gamedraw.get_rect(center = (350, 150))
            player_names.blit(gamedraw, gamedraw_rect)
            turn = 0

        pygame.display.update()
        clock.tick(frame_limit)

        if turn == 0:
            # for i in range(1000):
                # pygame.quit()
                return result

# Player Initialisation
players = [(rand_strat, "Rand1"), (rand_strat, "Rand2")]

# Plotting - Labels, Value Initialisation, Colours
labels = ["Draw", players[0][1], players[1][1]]
values = [0, 0, 0]
colors = [(0, 0x23, 0x28), (0xde, 0x04, 0x04), (0xe2, 0xd7, 0x0c)]
colors = list(map(lambda x : tuple(map(lambda y : y/0xff, x)), colors))

# Load Window
pygame.init()
pygame.display.set_caption("Connect Four")
screen = pygame.display.set_mode((700, 900)) # create screen

# Run Games
for i in range(100):
    print("Game No:", i+1)
    values[run_game(screen, players[0], players[1])] += 1

pygame.quit() # Close Window

# Plot Results
plt.bar(labels, values, color=colors)
plt.show()