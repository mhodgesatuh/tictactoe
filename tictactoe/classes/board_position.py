#!/usr/bin/env python
#pylint: disable=import-error
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

    def __init__(self, position_idx, width):
        """
        Initialize the board position.
        """
        self.position_idx = position_idx
        self.marked_by = ""
        self.corner_position = False

        position_no = position_idx + 1

        # Initially display the digits 1 through 9.
        self.position_display = str(position_no)

        # Determine if this is a corner position: 1, 3, 7, 9 by using
        # the board width to calculate the corners.
        for i in range(1, width):
            right_corner_no = width**i
            # Check for a left or right corner match.
            if position_no in [right_corner_no - width + 1, right_corner_no]:
                self.corner_position = True
                break

    def is_available(self):
        """
        Return true if the position has been marked, otherwise false.
        """
        return self.marked_by == ""

    def is_available_corner(self):
        """
        Return true if the position is an available corner.
        """
        return self.is_corner() and self.is_available()

    def is_corner(self):
        """
        Return true if the position is a one of the corners.
        """
        return self.corner_position

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
