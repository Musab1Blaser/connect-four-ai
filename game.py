import pygame
import random

def rand_strat(game_state, options):
    return random.sample(options, 1)

def draw_circles(board_sprite, game_state):
    for i in range(len(game_state)):
        for j in range(len(game_state[0])):
            if game_state[i][j] == 0:
                color = (0, 0, 0, 0)
            elif game_state[i][j] == 1:
                color = (0xde, 0x04, 0x04)
            elif game_state[i][j] == 2:
                color = (0xe2, 0xd7, 0x0c)
            pygame.draw.circle(board_sprite, color, (100*j+50, 100*i+50), 40) # 50, 150, ..., 650 -> last pix: 700


def run_game(strat1, start_name1,  strat2, strat_name2): # provide the two strategy functions
    game_state = [[i//2]*7 for i in range(6)] # generate empty board
    
    # pygame iniialisation
    pygame.init()
    clock = pygame.time.Clock()

    bg_color = (0, 0x23, 0x28)
    screen = pygame.display.set_mode((700, 900)) # create screen
    screen.fill(bg_color)

    board_color = (0, 0x54, 0x61) 
    board_sprite = pygame.Surface((700, 600), pygame.SRCALPHA) # create board with background
    board_rect = board_sprite.get_rect(topleft = (0, 300))
    board_sprite.fill(board_color)
    draw_circles(board_sprite, game_state) # fill in circles/clear circle spaces
            
    # board_sprite2 = pygame.Surface((100, 200), pygame.SRCALPHA)
    # board_sprite2.fill((200,100,100,200))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        screen.blit(board_sprite, board_rect)
        # screen.blit(board_sprite2, (0, 50))
        pygame.display.update()
        clock.tick(60)


run_game(rand_strat, "Rand1", rand_strat, "Rand2")