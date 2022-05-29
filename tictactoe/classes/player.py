#!/usr/bin/env python
#pylint: disable=import-error
"""
Project: TicTacToe - class exercise, OOPs version
"""
class Player:
    """
    The game play: this is a turn-based game with a board and two
    players.
    """

    # ---------------
    # Class functions
    # ---------------

    def __init__(self, player_mark, computer_player=False):
        """
        Initialize a player.  Set the player mark for the game board and
        indicate if the player is the computer or is a human that will
        be typing in the moves.
        """
        self.mark = player_mark
        self.computer_player = computer_player

    def __repr__(self):
        """
        The player's mark is the string representation of the player
        object.
        """
        return f'{self.mark}-Computer' if self.is_computer()\
            else f'{self.mark}-Human'

    def is_computer(self):
        """
        Return true if this is a computer player.
        """
        return self.computer_player
