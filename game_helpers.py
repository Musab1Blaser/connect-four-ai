import pygame
import random
import matplotlib.pyplot as plt

from basic_strats import rand_strat, player_strat

def check_win(game_state, turn, debug_mode = False):
    # row wise checking
    for i in range(len(game_state)):
        continuous = 0 # check for 4 contiguous in a row
        for j in range(len(game_state[0])):
            if game_state[i][j] == turn: # match
                continuous += 1
            else:
                continuous = 0 # matching failed - restart matching

            if continuous == 4: # matched successfully
                if debug_mode:
                    print("Horizonal Win!") 
                return True

    # column wise checking
    for j in range(len(game_state[0])):
        continuous = 0 # check for 4 contiguous in a row
        for i in range(len(game_state)):
            if game_state[i][j] == turn: # match
                continuous += 1
            else:
                continuous = 0 # matching failed - restart matching

            if continuous == 4: # matched successfully
                if debug_mode:
                    print("Vertical Win!")
                return True

    # main diagonal checking
    for h in range(-3, 3): # iterate through possible diagonals
        i, j = max(0, h), max(0, -h) # starting points of each diagonal
        continuous = 0 # check for 4 contiguous in a row
        while i < len(game_state) and j < len(game_state[0]):
            if game_state[i][j] == turn: # match
                continuous += 1
            else:
                continuous = 0 # matching failed - restart matching

            if continuous == 4: # matched successfully
                if debug_mode:
                    print("Main Diagonal Win!")
                return True

            i += 1
            j += 1

    # off diagonal checking
    for h in range(-3, 3): # iterate through possible diagonals
        i, j = max(0, h), min(6, 6 + h) # starting points of each diagonal
        continuous = 0 # check for 4 contiguous in a row
        while i < len(game_state) and j >= 0:
            if game_state[i][j] == turn:
                continuous += 1 # match
            else:
                continuous = 0 # matching failed - restart matching

            if continuous == 4: # matched successfully
                if debug_mode:
                    print("Off Diagonal Win!")
                return True

            i += 1
            j -= 1

    return False

def check_win_visual(clock, screen, player_names, player_rect, board_sprite, board_rect, game_state, turn):
    animation_speed = 10

    # row wise checking
    draw_board(screen, player_names, player_rect, board_sprite, board_rect, game_state)
    pygame.display.update()
    for i in range(len(game_state)):
        continuous = 0
        for j in range(len(game_state[0])):
            pygame.draw.circle(screen, (0x0, 0xff, 0x0), (50 + 100 * j, 350 + 100 * i), 40)
            pygame.display.update()
            clock.tick(animation_speed)
            if game_state[i][j] == turn:
                pygame.draw.circle(screen, (0x0, 0xaa, 0xaa), (50 + 100 * j, 350 + 100 * i), 40)
                pygame.display.update()
                continuous += 1
            else:
                continuous = 0

            if continuous == 4:
                print("Horizonal Win!")
                return True

    # column wise checking
    draw_board(screen, player_names, player_rect, board_sprite, board_rect, game_state)
    pygame.display.update()
    for j in range(len(game_state[0])):
        continuous = 0
        for i in range(len(game_state)):
            pygame.draw.circle(screen, (0x0, 0xff, 0x0), (50 + 100 * j, 350 + 100 * i), 40)
            pygame.display.update()
            clock.tick(animation_speed)
            if game_state[i][j] == turn:
                pygame.draw.circle(screen, (0x0, 0xaa, 0xaa), (50 + 100 * j, 350 + 100 * i), 40)
                pygame.display.update()
                continuous += 1
            else:
                continuous = 0

            if continuous == 4:
                print("Vertical Win!")
                return True

    # main diagonal checking
    draw_board(screen, player_names, player_rect, board_sprite, board_rect, game_state)
    pygame.display.update()
    for h in range(-3, 3):
        i, j = max(0, h), max(0, -h)
        continuous = 0
        while i < len(game_state) and j < len(game_state[0]):
            pygame.draw.circle(screen, (0x0, 0xff, 0x0), (50 + 100 * j, 350 + 100 * i), 40)
            pygame.display.update()
            clock.tick(animation_speed)
            if game_state[i][j] == turn:
                pygame.draw.circle(screen, (0x0, 0xaa, 0xaa), (50 + 100 * j, 350 + 100 * i), 40)
                pygame.display.update()
                continuous += 1
            else:
                continuous = 0

            if continuous == 4:
                print("Main Diagonal Win!")
                return True

            i += 1
            j += 1

    # off diagonal checking
    draw_board(screen, player_names, player_rect, board_sprite, board_rect, game_state)
    pygame.display.update()
    for h in range(-3, 3):
        i, j = max(0, h), min(6, 6 + h)
        continuous = 0
        while i < len(game_state) and j >= 0:
            pygame.draw.circle(screen, (0x0, 0xff, 0x0), (50 + 100 * j, 350 + 100 * i), 40)
            pygame.display.update()
            clock.tick(animation_speed)
            if game_state[i][j] == turn:
                pygame.draw.circle(screen, (0x0, 0xaa, 0xaa), (50 + 100 * j, 350 + 100 * i), 40)
                pygame.display.update()
                continuous += 1
            else:
                continuous = 0

            if continuous == 4:
                print("Off Diagonal Win!")
                return True

            i += 1
            j -= 1

    return False

def draw_circles(board_sprite, game_state):
    for i in range(len(game_state)):
        for j in range(len(game_state[0])):
            if game_state[i][j] == 0:
                color = (0, 0, 0, 0) # no player = empty
            elif game_state[i][j] == 1:
                color = (0xde, 0x04, 0x04) # player 1 = red
            elif game_state[i][j] == 2:
                color = (0xe2, 0xd7, 0x0c) # player 2 = yellow

            pygame.draw.circle(board_sprite, color, (100*j+50, 100*i+50), 40) # 50, 150, ..., 650 -> last pix: 700

def draw_board(screen, player_names, player_rect, board_sprite, board_rect, game_state, new_circle_pos = (), turn = 1):
    bg_color = (0, 0x23, 0x28)
    board_color = (0, 0x54, 0x61)

    screen.fill(bg_color)

    screen.blit(player_names, player_rect)

    if turn == 1:
        ball_color = (0xde, 0x04, 0x04) # player 1 = red
    elif turn == 2:
        ball_color = (0xe2, 0xd7, 0x0c) # player 2 = yellow

    if len(new_circle_pos):
        pygame.draw.circle(screen, ball_color, new_circle_pos, 40) # draw the falling ball

    board_sprite.fill(board_color)
    draw_circles(board_sprite, game_state) # fill in circles/clear circle spaces
    screen.blit(board_sprite, board_rect)
