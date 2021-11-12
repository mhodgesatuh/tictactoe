#!/usr/bin/env python
#pylint: disable=too-few-public-methods
"""
Project: TicTacToe - class exercise, OOPs version
"""
from random import randrange

class GameBoard:
    """
    The game board.  Holds and displays the current state of the game.
    """

    # ---------------
    # Class constants
    # ---------------

    # Graphics for displaying the game board.
    #  ruler:       123*567 123*567 123*567
    BOARD_LINER = '+-------+-------+-------+'
    BOARD_SPACE = '|       |       |       |'
    BOARD_MOVES = '|   {}   |   {}   |   {}   |'

    BOARD_WIDTH = 3

    # ---------------
    # Class functions
    # ---------------

    def __init__(self, player_marks):
        """
        Initialize the game board; all positions are initially available.
            0: [1, 2, 3]
            1: [4, 5, 6]
            2: [7, 8, 9]
        """
        self.player_marks = player_marks
        self.positions = [
            [self.BOARD_WIDTH * row_idx + col_idx + 1\
                for col_idx in range(self.BOARD_WIDTH)]\
                    for row_idx in range(self.BOARD_WIDTH)]

    def calculate_next_move(self, player):
        """
        Calculate the computer's move.
        """
        available_positions = self.get_available_positions()
        available_positions_count = len(available_positions)
        if available_positions_count > 0:
            # Randomly select an available position.
            random_move = randrange(available_positions_count)
            row, col = available_positions[random_move]
            self.mark_position(row, col, player)

    def display_positions(self):
        """
        Display the current board.
        """
        for row_idx in range(self.BOARD_WIDTH):
            print(self.BOARD_LINER)
            print(self.BOARD_SPACE)
            print(self.BOARD_MOVES.format(
                self.positions[row_idx][0],
                self.positions[row_idx][1],
                self.positions[row_idx][2]))
            print(self.BOARD_SPACE)
        print(self.BOARD_LINER)

    def is_game_over(self, player):
        """
        If a three-in-a-row win is detected return True.
        """
        diagonal_1 = True
        diagonal_2 = True
        for idx in range(3):
            # Check each row for a win.
            if self.positions[idx][0] == player.mark and\
                    self.positions[idx][1] == player.mark and\
                    self.positions[idx][2] == player.mark:
                return True
            # Check each column for a win.
            if self.positions[0][idx] == player.mark and\
                    self.positions[1][idx] == player.mark and\
                    self.positions[2][idx] == player.mark:
                return True
            # Check each diagonal for a win.
            if diagonal_1:
                if self.positions[idx][idx] != player.mark:
                    diagonal_1 = False
            if diagonal_2:
                if self.positions[2 - idx][2 - idx] != player.mark:
                    diagonal_2 = False
        return diagonal_1 or diagonal_1

    def get_available_positions(self):
        """
        Get a list of the remaining available positions.
        """
        available_positions = []
        for row_idx in range(self.BOARD_WIDTH):
            for col_idx in range(self.BOARD_WIDTH):
                if self.positions[row_idx][col_idx] not in self.player_marks:
                    available_positions.append((row_idx, col_idx))
        return available_positions

    def mark_position(self, row_idx, col_idx, player):
        """
        Place the player's mark into the selected position.
        """
        self.positions[row_idx][col_idx] = player.mark

    def request_next_move(self, player):
        """
        Request the human player's move.
        """
        valid_move = False
        while not valid_move:
            player_move = input("Enter your move: ")
            if not self.valid_players_move(player_move):
                print("Bad move, try again")
                continue
            player_move = int(player_move) - 1
            selected_row = player_move // 3
            selected_col = player_move % 3
            if not str(self.positions[selected_row][selected_col]).isdigit():
                print("Already taken, try again")
                continue
            valid_move = True
        self.mark_position(selected_row, selected_col, player)

    @staticmethod
    def valid_players_move(player_move):
        """
        Validate that the player picked an available position that is on
        the board.
        """
        return player_move.isdigit() and 1 <= int(player_move) <= 9
