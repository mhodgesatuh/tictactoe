#!/usr/bin/env python
#pylint: disable=import-error
"""
Project: TicTacToe - class exercise, OOPs version
"""

class BoardStripe:
    """
    The game board is composed of nine positions in 3 rows of 3 positions.
    Game play is across the three rows and the two diagonals, for a total
    of 5 stripes, for lack of a better terminology.
    """

    # ---------------
    # Class functions
    # ---------------

    def __init__(self, board_width):
        """
        Initialize the stripe.
        """
        self.positions = []
        self.corner_positions = False
        self.board_width = board_width

    def add_position(self, position):
        """
        Add the position to the stripe.
        """
        self.positions.append(position)
        if position.is_corner():
            self.corner_positions = True

    def get_available_corner_positions(self):
        """
        Return a list of available corner positions.
        """
        return self.get_available_positions(True)

    def get_available_positions(self, corners_only=False):
        """
        Return a list of available positions.
        """
        positions_found = []
        for idx in range(self.board_width):
            if corners_only and not self.positions[idx].is_corner():
                continue
            if self.positions[idx].is_available():
                positions_found.append(self.positions[idx])
        return positions_found


    def has_available_position(self):
        """
        Stripe has at least one available position.
        """
        for idx in range(self.board_width):
            if self.positions[idx].is_available():
                return True
        return False

    def has_corner_positions(self):
        """
        Return true if the stripe has corner positions.
        """
        return self.corner_positions

    def has_n_player_marks(self, player, n_marks):
        """
        A single player has 'n' marks in a stripe.  Used for identifying
        the number of marks a player has thus far.  If a stripe has the
        other players mark in it, it's no longer useful.
        """
        marks_found_cnt = 0
        for idx in range(self.board_width):
            if self.positions[idx].is_marked_by(player):
                marks_found_cnt += 1
            elif not self.positions[idx].is_available():
                # The other player has marked in this stripe.
                return False
        return marks_found_cnt == n_marks
