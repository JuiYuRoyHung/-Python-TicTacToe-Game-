import random

tictactoe_board = [0,0,0,0,0,0,0,0,0]

for gameround in range(1,10):
    #circule round
    for circule_try in range(1,10):
        circule_idx = random.randint(0,8)
        if tictactoe_board[circule_idx] == 1:
            print('already written circule')
            continue
        elif tictactoe_board[circule_idx] == 2:
            print('already written by cross')
            continue
        elif tictactoe_board[circule_idx] == 0:
            tictactoe_board[circule_idx] = 1
            break
    print('',tictactoe_board[0:3],'\n',tictactoe_board[3:6],'\n',tictactoe_board[6:],'\n')



    #circule check
    if tictactoe_board[0] == 1 & tictactoe_board[1] == 1  & tictactoe_board[2] == 1:
        print('Circule Win!!')
        break
    elif tictactoe_board[3] == 1 & tictactoe_board[4] == 1  & tictactoe_board[5] == 1:
        print('Circule Win!!')
        break
    elif tictactoe_board[6] == 1 & tictactoe_board[7] == 1  & tictactoe_board[8] == 1:
        print('Circule Win!!')
        break
    elif tictactoe_board[0] == 1 & tictactoe_board[3] == 1  & tictactoe_board[6] == 1:
        print('Circule Win!!')
        break
    elif tictactoe_board[1] == 1 & tictactoe_board[4] == 1  & tictactoe_board[7] == 1:
        print('Circule Win!!')
        break
    elif tictactoe_board[2] == 1 & tictactoe_board[5] == 1  & tictactoe_board[8] == 1:
        print('Circule Win!!')
        break
    elif tictactoe_board[0] == 1 & tictactoe_board[4] == 1  & tictactoe_board[8] == 1:
        print('Circule Win!!')
        break
    elif tictactoe_board[2] == 1 & tictactoe_board[4] == 1  & tictactoe_board[6] == 1:
        print('Circule Win!!')
        break



    
    #cross round
    for cross_try in range(1,10):
        cross_idx = random.randint(0,8)
        if tictactoe_board[cross_idx] == 1:
            print('already written circule')
            continue
        elif tictactoe_board[cross_idx] == 2:
            print('already written by cross')
            continue
        elif tictactoe_board[cross_idx] == 0:
            tictactoe_board[cross_idx] = 2
            break
    print('',tictactoe_board[0:3],'\n',tictactoe_board[3:6],'\n',tictactoe_board[6:],'\n')

    #cross check
    if tictactoe_board[0] == 2 & tictactoe_board[1] == 2  & tictactoe_board[2] == 2:
        print('Cross Win!!')
        break
    elif tictactoe_board[3] == 2 & tictactoe_board[4] == 2  & tictactoe_board[5] == 2:
        print('Cross Win!!')
        break
    elif tictactoe_board[6] == 2 & tictactoe_board[7] == 2  & tictactoe_board[8] == 2:
        print('Cross Win!!')
        break
    elif tictactoe_board[0] == 2 & tictactoe_board[3] == 2  & tictactoe_board[6] == 2:
        print('Cross Win!!')
        break
    elif tictactoe_board[1] == 2 & tictactoe_board[4] == 2  & tictactoe_board[7] == 2:
        print('Cross Win!!')
        break
    elif tictactoe_board[2] == 2 & tictactoe_board[5] == 2  & tictactoe_board[8] == 2:
        print('Cross Win!!')
        break
    elif tictactoe_board[0] == 2 & tictactoe_board[4] == 2  & tictactoe_board[8] == 2:
        print('Cross Win!!')
        break
    elif tictactoe_board[2] == 2 & tictactoe_board[4] == 2  & tictactoe_board[6] == 2:
        print('Cross Win!!')
        break

# Action Item
# 1. How to print O or X
# 2. If already board full, stop game
# 3. User vs robot interface
# 4. robot learning to play the game
