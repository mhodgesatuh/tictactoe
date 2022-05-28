#!/usr/bin/env python3
#pylint: disable=import-error
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
        self.board = GameBoard()
        self.move_calculator = MoveCalculator(self.board)
        self.players = []
        self.players.append(Player(self.PLAYER_MARKS[0], computer_player=True))
        self.players.append(Player(self.PLAYER_MARKS[1]))
        self.players_cnt = len(self.players)
        self.turn_count = 1

    @staticmethod
    def end_game(winning_player):
        """
        Declare the winner, or a tie, and end the game.
        """
        if winning_player is None:
            print("Game over, tie!")
        elif winning_player.is_computer():
            print("Game over, the compute won")
        else:
            print("Game over, you won!")

    def get_current_player(self):
        """
        Get the current player by turn count.
        """
        return self.players[(self.turn_count - 1) % self.players_cnt]

    def get_next_player(self):
        """
        Determine the index of the player taking the next turn.
        """
        return self.players[self.turn_count % self.players_cnt]

    def is_current_player_computer(self):
        """
        Return true if the current player is a computer.
        """
        return self.get_current_player().is_computer()

    def play_game_return_winner(self):
        """
        Start with the computer and begin taking turns.
        """
        winning_player = self.take_turns_return_winner()
        self.end_game(winning_player)

    def take_turns_return_winner(self):
        """
        Human and computer take turns.  Computer takes the first move.
        The current player is determined using modulo on the turn count.
        """
        # Take turns until there is a winner or no open positions
        # remain.
        winning_player = None
        while self.board.has_available_positions():
            self.board.display_positions()
            # Get next move.
            if self.is_current_player_computer():
                print('Computer\'s move:')
                selected_position = self.move_calculator.calculate_move_for(
                    self.get_current_player(),
                    self.get_next_player(),
                    self.turn_count)
            else:
                # Human to input the next move.
                selected_position = self.board.request_next_move()
            # Update the game board.
            selected_position.set_marked_by(self.get_current_player())
            # Assess the move.
            if self.board.is_game_over(self.get_current_player()):
                # We have a winner.
                winning_player = self.get_current_player()
                break
            # The game continues.
            self.turn_count += 1

        self.board.display_positions()
        return winning_player
