import pygame
import random

def rand_strat(game_state, options):
    return random.sample(options, 1)

def run_game(strat1, strat2):
    pygame.init()
    game_state = [[0]*7 for i in range(6)]
    screen = pygame.display.set_mode((800, 800))
    # while True:




run_game(rand_strat, rand_strat)