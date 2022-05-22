#!/usr/bin/env python
#pylint: disable=too-few-public-methods
"""
Project: TicTacToe - class exercise, OOPs version
"""
from random import randrange

class SmartMoveCalculator:
    """
    Calculate the next move.
        Decision	                  Move
        ---------------------------   -----------------------
        turn 1	                      middle position
        turn 2	                      corner position
        turn 3+
        - row/dia with 2 self only    remaining position in stripe, win
        - row/dia with 2 other only	  remaining position in stripe, block win
        - row/dia with 1 self only	  opposite end of stripe
        - any unmarked position
    """

    # ---------------
    # Class functions
    # ---------------

    def __init__(self, board):
        """
        Smart move calculator.
        """

        # Dependency injection.
        self.board = board

    def calculate_move_for(self, player, turn_count):
        """
        Calculate and perform the next move.
        """
        # First and second turns.
        if turn_count <= 2:

            # Check first to see if the center position is open.
            position = self.board.get_center_position()
            if position.is_available():
                return position

            # Randomly choose one of the two diagonals.
            stripe_idx = self.board.forward_diagonal_stripe_index + randrange(1)
            # Randomly choose one of the two ends of the diagonal.
            pos_idx = randrange(0, 2, 3)
            return self.board.stripes[stripe_idx].positions[pos_idx]

        # Check for stripes with 2 marks in order to win or block a win.
        # Then check for stripes with 1 mark.
        for n_marks in range(2, 0, -1):
            stripes = self.board.get_stripes_with_n_player_marks(player, n_marks)
            if len(stripes) > 0:
                return self.get_random_available_position(stripes)

        # Any open corner position will do at this point.
        corner_positions = self.board.get_available_corner_positions()
        if len(corner_positions) > 0:
            pos_idx = randrange(len(corner_positions))
            return corner_positions[pos_idx]

        # Any stray open position will do at this point.
        stripes = self.board.get_stripes_with_available_positions()
        return self.get_random_available_position(stripes)

    def get_random_available_position(self, stripes):
        """
        Once a filtered set of stripes matching the requirements is
        found, randomly choose a position from one of them to help avoid
        gameplay monotony.
        """
        # Randomly choose one of the matching stripes.
        stripe_idx = randrange(len(stripes))
        stripe = self.board.stripes[stripe_idx]

        # Randomly choose one of the available positions.
        available_positions = stripe.get_available_positions()
        pos_idx = randrange(len(available_positions))
        return stripe.positions[pos_idx]
