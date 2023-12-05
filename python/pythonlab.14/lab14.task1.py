from random import randint
def ShowBoard(board):
    blankBoard="""
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""

    for i in range(1,10):
        if (board[i] == 'O' or board[i] == 'X'):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)

def place_marker(board, marker, position):
    board[position] = marker
    return board

def space_check(board, position):
    return board[position] == '#'

def full_board_check(board):
    return len([x for x in board if x == '#']) == 1

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False

def HumanMove(board):
    choice = input("Please select an empty space between 1 and 9 : ")
    while not space_check(board, int(choice)):
        choice = input("This space isn't free. Please choose between 1 and 9 : ")
    return choice
def ComputerMove(board):
    choice = randint(1,9)
    while not space_check(board, int(choice)):
        choice = randint(1,9)
        print("This space isn't free. Computer is trying to place another mark")
    return choice
"""def replay():
    playAgain = input("Do you want to play again (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':
        return False"""

if __name__ == "__main__":
    i = 1
    player = "O"
    computer = "X"
    board = ['#'] * 10
    while True:
        game_on = full_board_check(board)
        while not game_on:
            if i % 2 == 0:
                position = HumanMove(board)
            else:
                position = ComputerMove(board)
            if i % 2 == 0:
                marker = player
            else:
                marker = computer
            place_marker(board, marker, int(position))
            ShowBoard(board)
            i += 1
            if win_check(board, marker):
                print("You won !")
                break
            game_on=full_board_check(board)
        """if not replay():
            break
        else:
            i = 1
            players=player_input()
            board = ['#'] * 10"""
