#!/usr/bin/env python3
"""
Project: TicTacToe - class exercise, OOPs version
"""
from tictactoe.classes.game_board import GameBoard
from tictactoe.classes.player import Player
from tictactoe.classes.smart_move_calculator import SmartMoveCalculator\
    as MoveCalculator

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
        self.turn_count = 1

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
            print("Game over, you beat the computer!")

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
        Human and computer take turns.  Computer takes the first move.
        """
        # Take turns until there is a winner or no open positions
        # remain.
        winning_player = None
        while self.game_board.has_available_positions:
            self.game_board.display_positions()
            current_player = self.get_next_player()
            # Get next move.
            if current_player.is_computer:
                print('Computer\'s move:')
                MoveCalculator(self.game_board, current_player)
            else:
                # Human to input the next move.
                self.game_board.request_next_move(current_player)
            # Assess the move.
            if self.game_board.is_game_over(current_player):
                # We found 3 in a row, game over.
                winning_player = current_player
                self.game_board.display_positions()
                break
            self.turn_count += 1
        return winning_player
