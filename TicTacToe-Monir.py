# TicTacToe - easy implementation to get started
# Your task is to write a simple program which pretends to play
# tic-tac-toe with a human player. To make it all easier for you, we've
# decided to simplify the game. Here are our assumptions:
# 1) The computer (i.e., your program) should play the game using 'X's;
#    the human player (e.g., you) should play the game using 'O's; the
#    first move belongs to the computer - it always puts its first 'X' in
#    the middle of the board.
# 2) All the squares are numbered row by row starting with 1 (see the
#    example session below for reference) the human player inputs their
#    move by entering the number of the square they choose - the number
#    must be valid, i.e., it must be an integer, it must be > than 0 and
#    < than 10, and it cannot point to a field which is already occupied:
#    the program checks if the game is over.
# 3) There are four possible verdicts: the game should continue, or the
#    game ends with a tie, your win, or the computer's win; the computer
#    responds with its move and the check is repeated.
# 4) Don't implement any form of artificial intelligence - a random
#    field choice made by the computer is good enough for the game.
from random import randrange

HUMAN_PLAYER = 'O'
COMPUTER_PLAYER = 'X'
GAME_PLAYERS = [HUMAN_PLAYER, COMPUTER_PLAYER]

# Graphics for displaying the game board.
# ruler:        123*567 123*567 123*567
BOARD_LINER = '+-------+-------+-------+'
BOARD_SPACE = '|       |       |       |'
BOARD_MOVES = '|   {}   |   {}   |   {}   |'

def calculateNextMove(game_board):
    """
    Calculate the next move.
    """
    print('Computer\'s move:')
    available_moves = getAvailableMoves(game_board)
    available_movesCount = len(available_moves)
    if available_movesCount > 0:
        # Randomly select an available move.
        random_move = randrange(available_movesCount)
        row, col = available_moves[random_move]
        game_board[row][col] = COMPUTER_PLAYER

def displayGameBoard(game_board):
    """
    Display the current board.
    """
    for row_idx in range(len(game_board)):
        print(BOARD_LINER)
        print(BOARD_SPACE)
        print(BOARD_MOVES.format(
            game_board[row_idx][0],
            game_board[row_idx][1],
            game_board[row_idx][2]
        ))
        print(BOARD_SPACE)
    print(BOARD_LINER)
    return game_board

def getAvailableMoves(game_board):
    """
    Get a list of the remaining available moves.
    """
    available_moves = []
    for row_idx in range(3):
        for col_idx in range(3):
            if game_board[row_idx][col_idx] not in GAME_PLAYERS:
                available_moves.append((row_idx, col_idx))
    return available_moves

def getNewGameBoard():
    """
    Prepare new game board.
    """
    return [[
            3 * row_idx + col_idx + 1 for col_idx in range(3)
        ] for row_idx in range(3)
    ]

def gameIsOver(game_board, player):
    """
    If a victory is detected return True.
    """
    diagonal_1 = True
    diagonal_2 = True
    for idx in range(3):
        # Check each row for a win.
        if game_board[idx][0] == player and\
                game_board[idx][1] == player and\
                game_board[idx][2] == player:
            return True
        # Check each column for a win.
        if game_board[0][idx] == player and\
                game_board[1][idx] == player and\
                game_board[2][idx] == player:
            return True
        # Check each diagonal for a win.
        if diagonal_1:
            if game_board[idx][idx] != player:
                diagonal_1 = False
        if diagonal_2:
            if game_board[2 - idx][2 - idx] != player:
                diagonal_2 = False
    return True if diagonal_1 or diagonal_1 else False

def requestNextMove(game_board):
    """
    Handle taking turns between each of the players.
    """
    valid_move = False
    while not valid_move:
        player_move = input("Enter your move: ")
        if not validUsersMove(player_move):
            print("Bad move, try again")
            continue
        player_move = int(player_move) - 1
        selected_row = player_move // 3
        selected_col = player_move % 3
        if game_board[selected_row][selected_col] in GAME_PLAYERS:
            print("Already taken, try again")
            continue
        valid_move = True
    game_board[selected_row][selected_col] = HUMAN_PLAYER

def validUsersMove(player_move):
    """
    Validate that the player picked a move that is on the board.
    """
    return True if player_move.isdigit() and\
        1 <= int(player_move) <= 9 else False

# -----------------
# Game begins here.
# -----------------

# Set up the game board.
game_board = getNewGameBoard()

# The computer gets the first move and always chooses the center.
game_board[1][1] = COMPUTER_PLAYER
available_moves = getAvailableMoves(game_board)

# Human and computer turns.  Computer has taken the first move to
# select the middle of the board.
victor = None
human_turn = True
while len(available_moves):
    displayGameBoard(game_board)
    # Get next move.
    if human_turn:
        player = HUMAN_PLAYER
        requestNextMove(game_board)
    else:
        player = COMPUTER_PLAYER
        calculateNextMove(game_board)
    # Assess next move.
    if gameIsOver(game_board, player):
        # We found 3 in a row, game over,
        victor = player
        displayGameBoard(game_board)
        break
    human_turn = not human_turn
    available_moves = getAvailableMoves(game_board)

# End game.
if victor == HUMAN_PLAYER:
    print("Game over, you won!")
elif victor == COMPUTER_PLAYER:
    print("Game over, the compute won")
else:
    print("Game over, tie!")
