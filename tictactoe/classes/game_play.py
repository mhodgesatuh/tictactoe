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
        self.board = GameBoard()
        self.move_calculator = MoveCalculator(self.board)
        self.players = []
        self.players.append(Player(self.PLAYER_MARKS[0], is_computer=True))
        self.players.append(Player(self.PLAYER_MARKS[1]))
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
        Human and computer take turns.  Computer takes the first move.
        """
        # Take turns until there is a winner or no open positions
        # remain.
        winning_player = None
        while self.board.has_available_positions():
            self.board.display_positions()
            current_player = self.get_next_player()
            # Get next move.
            if current_player.is_computer:
                print('Computer\'s move:')
                selected_position = self.move_calculator.calculate_move_for(
                    current_player,
                    self.turn_count)
            else:
                # Human to input the next move.
                selected_position = self.board.request_next_move()
            # Update the game board.
            selected_position.set_marked_by(current_player)
            # Assess the move.
            if self.board.is_game_over(current_player):
                # We have a winner.
                winning_player = current_player
                self.board.display_positions()
                break
            self.turn_count += 1
        return winning_player
