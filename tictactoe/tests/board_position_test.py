#!/usr/bin/env python3
"""
Project: TicTacToe - class exercise, OOPs version
"""
from tictactoe.classes.board_position import BoardPosition
from tictactoe.classes.game_board import GameBoard
from tictactoe.classes.player import Player

class BoardPositionTest:
    """
    Board Position test harness.
    """
    test_board = GameBoard()
    test_player = Player('X', True)

    def init_corners_test(self):
        """
        Test the creation of the corner positions.
        """
        corner_idxs = [0, 2, 6, 8]
        for idx in corner_idxs:
            test_position = BoardPosition(idx, self.test_board.BOARD_WIDTH)
            assert test_position.is_corner()
            assert test_position.is_available_corner()
            assert not test_position.is_marked()
            assert test_position.position_display == str(idx + 1)

    def init_non_corners_test(self):
        """
        Test the creation of the non-corner positions.
        """
        non_corner_idxs = [1, 3, 4, 5, 7]
        for idx in non_corner_idxs:
            test_position = BoardPosition(idx, self.test_board.BOARD_WIDTH)
            assert not test_position.is_available_corner()
            assert not test_position.is_corner()
            assert not test_position.is_marked()
            assert test_position.is_available()
            assert test_position.position_display == str(idx + 1)

    def init_center_position_test(self):
        """
        Test that instantiation of a game board correctly instantiates
        the center position.
        """
        test_center_position = BoardPosition(4, self.test_board.BOARD_WIDTH)
        center_position = self.test_board.get_center_position()
        assert test_center_position.position_display ==\
            center_position.position_display

    def marked_by_test(self):
        """
        Test indicating that a player has selected (AKA marked) a position.
        """
        test_position = BoardPosition(4, self.test_board.BOARD_WIDTH)
        test_position.set_marked_by(self.test_player)
        assert not test_position.is_available()
        assert test_position.is_marked()
