import pygame
import random

from basic_strats import rand_strat, player_strat

def check_win(game_state, turn):
    # row wise checking
    for i in range(len(game_state)):
        continuous = 0 # check for 4 contiguous in a row
        for j in range(len(game_state[0])):
            if game_state[i][j] == turn: # match
                continuous += 1
            else:
                continuous = 0 # matching failed - restart matching

            if continuous == 4: # matched successfully
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

def run_game(strat1, start_name1,  strat2, strat_name2): # provide the two strategy functions
    game_state = [[0]*7 for i in range(6)] # generate empty board
    turn = 1
    
    # pygame iniialisation
    pygame.init()
    pygame.display.set_caption("Connect Four")
    clock = pygame.time.Clock()

    bg_color = (0, 0x23, 0x28)
    screen = pygame.display.set_mode((700, 900)) # create screen
    screen.fill(bg_color)

    # Player Names
    font = pygame.font.Font(None, 50)

    # Names Canvas
    player_names = pygame.Surface((700, 200), pygame.SRCALPHA)
    player_rect = player_names.get_rect(topleft = (0, 0))

    # Player 1 Canvas
    player1 = font.render(start_name1, True, (0xde, 0x04, 0x04))
    player1_rect = player1.get_rect(topleft = (20, 20))
    
    # Player 2 Canvas
    player2 = font.render(strat_name2, True, (0xe2, 0xd7, 0x0c))
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
        
        animation_speed = 4 # controls ball fall speed - recommended : 4
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
            if check_win(game_state, turn):
                print(f"Last Move: {turn} - {i}, {j}")
                turn = 0
            else:
                turn = 3 - turn
        
        pygame.display.update()
        clock.tick(60)

while True:
    run_game(rand_strat, "Rand1", player_strat, "Player")