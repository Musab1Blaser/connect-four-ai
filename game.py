import pygame
import random

def rand_strat(game_state, options):
    return random.sample(options, 1)

def run_game(strat1, strat2): # provide the two strategy functions
    game_state = [[0]*7 for i in range(6)] # generate empty board
    
    pygame.init()
    screen = pygame.display.set_mode((800, 800)) # create screen
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pygame.display.update()


run_game(rand_strat, rand_strat)