from game_helpers import check_win

def evaluate_state(game_state, turn):
    consec_freq = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
    # row wise checking
    for i in range(len(game_state)):
        my_continuous = 0 # check amount of contiguous
        other_continuous = 0
        for j in range(len(game_state[0])):
            if game_state[i][j] == turn: # match
                my_continuous += 1
            else:
                consec_freq[my_continuous] += 1
                my_continuous = 0 # matching failed - restart matching

            if game_state[i][j] == 3-turn: # match
                other_continuous += 1
            else:
                consec_freq[other_continuous] -= 1
                other_continuous = 0 # matching failed - restart matching
                
    consec_freq[my_continuous] += 1
    consec_freq[other_continuous] -= 1

    # column wise checking
    for j in range(len(game_state[0])):
        my_continuous = 0 # check for 4 contiguous in a row
        other_continuous = 0
        for i in range(len(game_state)):
            if game_state[i][j] == turn: # match
                my_continuous += 1
            else:
                consec_freq[my_continuous] += 1
                my_continuous = 0 # matching failed - restart matching

            if game_state[i][j] == 3-turn: # match
                other_continuous += 1
            else:
                consec_freq[other_continuous] -= 1
                other_continuous = 0 # matching failed - restart matching

    consec_freq[my_continuous] += 1
    consec_freq[other_continuous] -= 1

    # main diagonal checking
    for h in range(-3, 3): # iterate through possible diagonals
        i, j = max(0, h), max(0, -h) # starting points of each diagonal
        my_continuous = 0 # check for 4 contiguous in a row
        other_continuous = 0
        while i < len(game_state) and j < len(game_state[0]):
            if game_state[i][j] == turn: # match
                my_continuous += 1
            else:
                consec_freq[my_continuous] += 1
                my_continuous = 0 # matching failed - restart matching

            if game_state[i][j] == 3 - turn: # match
                other_continuous += 1
            else:
                consec_freq[other_continuous] -= 1
                other_continuous = 0 # matching failed - restart matching

            i += 1
            j += 1

    consec_freq[my_continuous] += 1
    consec_freq[other_continuous] -= 1

    # off diagonal checking
    for h in range(-3, 3): # iterate through possible diagonals
        i, j = max(0, h), min(6, 6 + h) # starting points of each diagonal
        my_continuous = 0 # check for 4 contiguous in a row
        other_continuous = 0
        while i < len(game_state) and j >= 0:
            if game_state[i][j] == turn:
                my_continuous += 1 # match
            else:
                consec_freq[my_continuous] += 1
                my_continuous = 0 # matching failed - restart matching

            if game_state[i][j] == 3 - turn:
                other_continuous += 1 # match
            else:
                consec_freq[other_continuous] -= 1
                other_continuous = 0 # matching failed - restart matching

            i += 1
            j -= 1

    consec_freq[my_continuous] += 1
    consec_freq[other_continuous] -= 1

    weightage = [0, 10, 30, 100, 10000]
    val = 0
    for i in range(4):
        val += weightage[i] * consec_freq[i]
    return val

def minimax_strat(game_state, options, turn):
    depth = 4
    return minimax_explore(game_state, options, turn, depth)[1]
        
def minimax_explore(game_state, options, turn, depth): # Find the value of my children state for me. Return the best strategy for me.
    results = [] # options and their values

    for i, j in options: # check each option
        game_state[i][j] = turn # make change

        if check_win(game_state, turn): # immediately accept if winning condition for me
            game_state[i][j] = 0
            return (10000, (i, j))
        
        if depth == 1: # base case - value of the state after this move
            results.append((evaluate_state(game_state, turn), (i, j)))

        else: # recursive case - explore game tree

            move_list = [] # generate subsequent move list
            for a in range(len(game_state[0])):
                for b in range(len(game_state)-1, -1, -1):
                    if game_state[b][a] == 0:
                        move_list.append((b, a))
                        break

            if len(move_list):
                res = minimax_explore(game_state, move_list, 3 - turn, depth - 1) # find best move for my enemy in this case
                results.append((-res[0], (i, j))) # value of my move for me is -ve of the final value for enemy
            else:
                results.append((0, (i, j))) # draw
        
        game_state[i][j] = 0 # undo change
        
    return max(results)