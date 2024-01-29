def evaluate_state(game_state, turn):
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