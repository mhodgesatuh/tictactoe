#!/usr/bin/env python
#pylint: disable=too-few-public-methods
"""
Project: TicTacToe - class exercise, OOPs version
"""

class BoardPosition:
    """
    The game board is composed of nine positions in 3 rows of 3
    positions.
    """

    # ---------------
    # Class functions
    # ---------------

    def __init__(self, position_idx):
        """
        Initialize the board position.
        """
        self.position_idx = position_idx
        self.marked_by = ""

        # Initially display the digits 1 through 9.
        self.position_display = str(position_idx + 1)

    def is_available(self):
        """
        Return true if the position has been marked, otherwise false.
        """
        return self.marked_by == ""

    def is_marked(self):
        """
        Return true if the position has been marked, otherwise false.
        """
        return not self.is_available()

    def is_marked_by(self, player):
        """
        Return true if the player has marked the position.
        """
        return self.marked_by == player

    def set_marked_by(self, player):
        """
        Save the player mark for this position.
        """
        self.marked_by = player
        self.position_display = player.mark
