import pygame
import random

def rand_strat(game_state, options):
    return random.sample(options, 1)

def run_game(strat1, strat2): # provide the two strategy functions
    game_state = [[0]*7 for i in range(6)] # generate empty board
    
    # pygame iniialisation
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((800, 800)) # create screen
    board_sprite = pygame.Surface((100, 200))
    board_sprite.fill((100,200,100,250))
    board_sprite2 = pygame.Surface((100, 200), pygame.SRCALPHA)
    board_sprite2.fill((200,100,100,200))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        screen.blit(board_sprite, (0, 0))
        screen.blit(board_sprite2, (0, 50))
        pygame.display.update()
        clock.tick(60)


run_game(rand_strat, rand_strat)