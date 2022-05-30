#!/usr/bin/env python
#pylint: disable=import-error
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

    def calculate_move_for(self, player, other_player, turn_count):
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
            stripe_idx = self.board.forward_diagonal_stripe_index + randrange(2)
            # Randomly choose one of the two ends, 0 or 2, of the diagonal.
            pos_idx = randrange(0, 3, 2)
            return self.board.stripes[stripe_idx].positions[pos_idx]

        # Check for stripes with 2 same-player marks in order to win or
        # block a win.  Then check for stripes with 1 mark.
        for n_marks in range(2, 0, -1):

            # Look for a win.
            stripes = self.board.get_stripes_with_n_player_marks(
                player,
                n_marks,
                turn_count)
            if len(stripes) > 0:
                # Return a winning position, or at least a good position.
                return self.get_random_available_position(stripes)

            # Look for blocking a win.
            if n_marks == 2:
                stripes = self.board.get_stripes_with_n_player_marks(
                    other_player,
                    n_marks,
                    turn_count)
                if len(stripes) > 0:
                    # Return a blocking position.
                    return self.get_random_available_position(stripes)

        # Any stray open position will do at this point.
        positions = self.board.get_available_positions()
        position_idx = randrange(len(positions))
        return positions[position_idx]

    @staticmethod
    def get_random_available_position(stripes):
        """
        Once a filtered set of stripes matching the requirements is
        found, randomly choose a position from one of them to help avoid
        gameplay monotony.
        """
        # Randomly choose one of the matching stripes.
        stripe_idx = randrange(len(stripes))
        stripe = stripes[stripe_idx]

        # Randomly choose a corner position, if available.
        available_corner_positions = stripe.get_available_corner_positions()
        if len(available_corner_positions) > 0:
            pos_idx = randrange(len(available_corner_positions))
            return available_corner_positions[pos_idx]

        # Randomly choose a any position, if available.
        available_positions = stripe.get_available_positions()
        pos_idx = randrange(len(available_positions))
        return available_positions[pos_idx]
