#!/usr/bin/env python3
#pylint: disable=import-error
"""
Project: TicTacToe - class exercise, OOPs version
"""
from tictactoe.classes.board_position import BoardPosition
from tictactoe.classes.board_stripe import BoardStripe
from tictactoe.classes.game_board import GameBoard
from tictactoe.classes.player import Player

class BoardStripeTest:
    """
    Board Position test harness.
    """
    test_board = GameBoard()
    test_player_x = Player('X', True)
    test_player_o = Player('O', True)

    def _create_test_stripe(self):
        """
        Helper to create a stripe suitable for testing.
        """
        test_stripe = BoardStripe(self.test_board.BOARD_WIDTH)
        for idx in range(self.test_board.BOARD_WIDTH):
            test_position = BoardPosition(idx, self.test_board.BOARD_WIDTH)
            test_stripe.add_position(test_position)
        return test_stripe

    def init_stripe_test(self):
        """
        Test initiation of a board stripe.
        """
        test_stripe = self._create_test_stripe()
        assert test_stripe.has_available_position()
        available_test_positions = test_stripe.get_available_positions()
        assert len(available_test_positions) == self.test_board.BOARD_WIDTH
        assert test_stripe.has_available_position()

    def n_marks_test(self):
        """
        Test stripe for 2 and 3 marks.
        """
        # Test a stripe with no X player marks.
        test_stripe = self._create_test_stripe()
        assert not test_stripe.has_n_player_marks(self.test_player_x, 1)

        # Test a stripe with 2 X player only marks.
        test_stripe.positions[1].set_marked_by(self.test_player_x)
        test_stripe.positions[2].set_marked_by(self.test_player_x)
        assert test_stripe.has_n_player_marks(self.test_player_x, 2)

        # Test a stripe with 2 X player and no "O" player mark.
        assert not test_stripe.has_n_player_marks(self.test_player_o, 2)

        # Test a stripe with 2 X player and 1 "O" player mark.
        test_stripe.positions[0].set_marked_by(self.test_player_o)
        assert not test_stripe.has_n_player_marks(self.test_player_x, 2)
        assert not test_stripe.has_n_player_marks(self.test_player_x, 3)

        # Test a stripe with 3 X player only marks.
        test_stripe.positions[0].set_marked_by(self.test_player_x)
        assert not test_stripe.has_n_player_marks(self.test_player_x, 2)
        assert test_stripe.has_n_player_marks(self.test_player_x, 3)

        # Test a stripe with 1 X player mark and 1 "O" player mark.
        test_stripe = self._create_test_stripe()
        test_stripe.positions[1].set_marked_by(self.test_player_x)
        test_stripe.positions[2].set_marked_by(self.test_player_o)
        assert not test_stripe.has_n_player_marks(self.test_player_x, 2)

    def no_available_positions_test(self):
        """
        Test for no avalable positions left in the stripe.
        """
        # No positions remaining test.
        test_stripe = self._create_test_stripe()
        for idx in range(self.test_board.BOARD_WIDTH):
            test_stripe.positions[idx].set_marked_by(self.test_player_x)
        available_test_positions = test_stripe.get_available_positions()
        assert len(available_test_positions) == 0
        assert not test_stripe.has_available_position()
