#!/usr/bin/env python3
#pylint: disable=import-error
"""
Project: TicTacToe - class exercise, OOPs version
"""
from tictactoe.classes.player import Player

class PlayerTest:
    """
    Player test harness.
    """

    @staticmethod
    def init_test():
        """
        Unit test
        """
        computer_player = Player('X', True)
        assert computer_player.mark == 'X'
        assert str(computer_player) == 'X-Computer'
        assert computer_player.is_computer()

        human_player = Player('O')
        assert human_player.mark == 'O'
        assert str(human_player) == 'O-Human'
        assert not human_player.is_computer()
