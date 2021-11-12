#!/usr/bin/env python
"""
Project: TicTacToe - class exercise, OOPs version
"""
from unittest.mock import patch
from IPython.utils.capture import capture_output
from tictactoe.classes.game_board import GameBoard
from tictactoe.classes.player import Player

class GameBoardTest:
    """
    Game board test harness.
    """
    game_board = GameBoard(['O', 'X'])
    test_player = Player('X')
    other_test_player = Player('O')

    @staticmethod
    def init_test():
        """
        Unit test
        """
        # Check for a 5 in the center position.
        game_board = GameBoard(['O', 'X'])
        assert game_board.positions[1][1] == 5

    def calculate_next_move_test(self):
        """
        Unit test
        """
        # Mark all positions but one (1,2), for the first player.
        game_board = GameBoard(['O', 'X'])
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 2:
                    # Save for other player.
                    continue
                game_board.mark_position(i, j, self.test_player)

        # Test that just position (1, 2) is available.
        available_positions = game_board.get_available_positions()
        assert len(available_positions) == 1
        assert available_positions[0] == (1, 2)

        # Test calculation of the next move for the other player.
        game_board.calculate_next_move(self.other_test_player)
        assert game_board.positions[1][2] == self.other_test_player.mark

    def display_positions_test(self):
        """
        Unit test
        """
        with capture_output() as captured:
            self.game_board.display_positions()
        captured()
        assert self.game_board.BOARD_LINER in captured.stdout
        assert self.game_board.BOARD_SPACE in captured.stdout

    def is_game_over_test(self):
        """
        Unit test
        """
        assert not self.game_board.is_game_over(self.test_player)

        # Check for horizontal three-in-a-row.
        game_board = GameBoard(['O', 'X'])
        for j in range(3):
            game_board.mark_position(0, j, self.test_player)
        assert game_board.is_game_over(self.test_player)

        # Check for vertical three-in-a-row.
        game_board = GameBoard(['O', 'X'])
        for i in range(3):
            game_board.mark_position(i, 2, self.test_player)
        assert game_board.is_game_over(self.test_player)

    @patch('builtins.input', lambda *args: '5')
    def request_next_move_test(self):
        """
        Unit test
        """
        game_board = GameBoard(['O', 'X'])
        game_board.request_next_move(self.test_player)
        assert game_board.positions[1][1] == self.test_player.mark

    @staticmethod
    def valid_players_move_test():
        """
        Unit test
        """
        game_board = GameBoard(['O', 'X'])
        assert game_board.valid_players_move('5')
        assert not game_board.valid_players_move('55')
        assert not game_board.valid_players_move('abc')
