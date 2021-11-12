#!/usr/bin/env python3
"""
Project: TicTacToe - class exercise, OOPs version
"""
from tictactoe.classes.game_board import GameBoard
from tictactoe.classes.player import Player

class GamePlay:
    """
    The game play: this is a turn-based game with a board and two
    players.
    """

    # ---------------
    # Class constants
    # ---------------

    PLAYER_MARKS = ['X', 'O']

    # ---------------
    # Class functions
    # ---------------

    def __init__(self):
        """
        Initialize the players and start the game.
        """
        self.current_player_idx = 0
        self.players = []
        self.players.append(Player(self.PLAYER_MARKS[0], is_computer=True))
        self.players.append(Player(self.PLAYER_MARKS[1]))
        self.game_board = GameBoard(self.PLAYER_MARKS)

    @staticmethod
    def end_game(winning_player):
        """
        Declare the winner, or a tie, and end the game.
        """
        if winning_player is None:
            print("Game over, tie!")
        elif winning_player.is_computer:
            print("Game over, the compute won")
        else:
            print("Game over, you won!")

    def get_next_player(self):
        """
        Determine the index of the player taking the next turn.
        """
        self.current_player_idx = 1 if self.current_player_idx == 0 else 0
        return self.players[self.current_player_idx]

    def play_game_return_winner(self):
        """
        Start with the computer and begin taking turns.
        """
        winning_player = self.take_turns_return_winner()
        self.end_game(winning_player)

    def take_turns_return_winner(self):
        """
        Human and computer take turns.  Computer takes the first move
        and always selects the middle of the board.
        """
        # The computer gets the first move and always chooses the
        # center.
        current_player = self.players[self.current_player_idx]
        self.game_board.mark_position(row_idx=1, col_idx=1, player=current_player)

        # Take turns until there is a winner or no open positions
        # remain.
        winning_player = None
        available_positions = self.game_board.get_available_positions()
        while available_positions:
            self.game_board.display_positions()
            current_player = self.get_next_player()
            # Get next move.
            if current_player.is_computer:
                print('Computer\'s move:')
                self.game_board.calculate_next_move(current_player)
            else:
                # Human to input the next move.
                self.game_board.request_next_move(current_player)
            # Assess the move.
            if self.game_board.is_game_over(current_player):
                # We found 3 in a row, game over.
                winning_player = current_player
                self.game_board.display_positions()
                break
            # Game continues.
            available_positions = self.game_board.get_available_positions()
        return winning_player
