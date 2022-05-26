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
    game_board = GameBoard()
    test_player = Player('X')
    other_test_player = Player('O')

    @staticmethod
    def init_test():
        """
        Unit test
        """
        # Check for a 5 in the center position.
        test_board = GameBoard()

        # Check positions creation.
        assert len(test_board.positions) == 9
        assert test_board.positions[4].position_idx == 4
        assert test_board.positions[4].position_display == "5"
        assert test_board.positions[4].marked_by == ""

        # Check stripes creation.
        assert len(test_board.stripes) == 8
        assert test_board.backward_diagonal_stripe_index == 7
        assert test_board.forward_diagonal_stripe_index == 6
        stripes_with_corners_cnt = 0
        for idx in range(len(test_board.stripes)):
            if test_board.stripes[idx].has_corner_positions():
                stripes_with_corners_cnt += 1
        assert stripes_with_corners_cnt == 6

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
        game_board = GameBoard()
        for position_idx in range(3):
            game_board.positions[position_idx].set_marked_by(self.test_player)
        assert game_board.is_game_over(self.test_player)

        # Check for vertical three-in-a-row.
        game_board = GameBoard()
        for i in range(3):
            position_idx = i * game_board.BOARD_WIDTH
            game_board.positions[position_idx].set_marked_by(self.test_player)
        assert game_board.is_game_over(self.test_player)

    @staticmethod
    def valid_players_move_test():
        """
        Unit test
        """
        game_board = GameBoard()
        assert game_board.valid_players_move('5')
        assert not game_board.valid_players_move('55')
        assert not game_board.valid_players_move('abc')
        assert not game_board.valid_players_move('abc')
