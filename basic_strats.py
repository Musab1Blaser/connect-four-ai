import pygame
import random

def rand_strat(game_state, options, turn): # pick a random column to place
    return random.choice(options)

def player_strat(game_state, options, turn): # place on player click
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # allow game exit
                pygame.quit()
                exit()

            elif pygame.mouse.get_pressed()[0]: # if mouse clicked
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[1] > 300: # and click within board
                    col = mouse_pos[0]//100 # find column
                    for ij in options:
                        if col == ij[1]: # if column has space then accept move
                            return ij