#!/usr/bin/env python
#pylint: disable=import-error
"""
Project: TicTacToe - class exercise, OOPs version
"""
from tictactoe.classes.board_position import BoardPosition as Position
from tictactoe.classes.board_stripe import BoardStripe as Stripe

class GameBoard:
    """
    The game board.  Holds and displays the current state of the game.
    """

    # ---------------
    # Class constants
    # ---------------

    # Graphics for displaying the game board.
    #  ruler:       123*567 123*567 123*567
    BOARD_LINER = '+-------+-------+-------+'
    BOARD_SPACE = '|       |       |       |'
    BOARD_MARKS = '|   {}   |   {}   |   {}   |'

    BOARD_WIDTH = 3

    # ---------------
    # Class functions
    # ---------------

    def __init__(self):
        """
        Initialize the game board; all positions are initially available.
            Display initial marks:
                [1, 2, 3]
                [4, 5, 6]
                [7, 8, 9]
            Where there are:
                9 board positions indexed 0 through 8
                8 stripes of 3 positions each:
                    row stripes - [1,2,3], [4,5,6], [7,8,9]
                    column stripes - [1,4,7], [2,5,8], [3,6,9]
                    diagonal stripes - [1,5,9], [3,5,7]
            A player must mark all of the positions in a single stripe
            to win a game.
        """
        self.positions = []
        self.stripes = []

        # Create the game board's positions and row stripes objects.
        stripe_idx = 0
        for i in range(self.BOARD_WIDTH):

            # Initial the row stripes.
            stripe = Stripe(self.BOARD_WIDTH)
            self.stripes.append(stripe_idx)
            self.stripes[stripe_idx] = stripe

            for j in range(self.BOARD_WIDTH):
                # Calculate the position index.
                position_idx = i * self.BOARD_WIDTH + j
                # Create the position.
                self.positions.append(position_idx)
                self.positions[position_idx] = Position(
                    position_idx,
                    self.BOARD_WIDTH
                    )
                # Save positions to row stripes.
                stripe.add_position(self.positions[position_idx])

            stripe_idx += 1

        # Create the game board's column stripes.
        for i in range(self.BOARD_WIDTH):
            stripe = Stripe(self.BOARD_WIDTH)
            self.stripes.append(stripe_idx)
            self.stripes[stripe_idx] = stripe

            for j in range(self.BOARD_WIDTH):
                # Calculate the position index.
                position_idx = i + self.BOARD_WIDTH * j
                # Save positions to column stripes.
                stripe.add_position(self.positions[position_idx])

            stripe_idx += 1

        # Create the game board's diagonal stripes.
        #
        #  - Backward diagonal:
        #       position indicies: [2,4,6]; calc using 2+i*2
        backward_stripe = Stripe(self.BOARD_WIDTH)
        self.stripes.append(backward_stripe)
        self.stripes[stripe_idx] = backward_stripe
        stripe_idx += 1
        #
        #  - Forward diagonal:
        #       position indicies: [0,4,8]; calc using i*4
        forward_stripe = Stripe(self.BOARD_WIDTH)
        self.stripes.append(stripe_idx)
        self.stripes[stripe_idx] = forward_stripe

        pos_offset = self.BOARD_WIDTH - 1
        for i in range(self.BOARD_WIDTH):
            # Save positions to the forward diagonal stripe.
            position = self.positions[i * pos_offset * 2]
            forward_stripe.add_position(position)
            # Save positions to the backward diagonal stripe.
            position = self.positions[pos_offset + i * pos_offset]
            backward_stripe.add_position(position)

        # Optimize the stripes for the smart move calculater by listing
        # the diagonal stripes first. Generally, moves on the stripes
        # are the stronger moves at the beginning of the game.
        self.stripes.reverse()
        self.forward_diagonal_stripe_index = 0
        self.backward_diagonal_stripe_index = 1

    def display_positions(self):
        """
        Display the current board.
        """
        for row_idx in range(self.BOARD_WIDTH):
            position_idx = row_idx * self.BOARD_WIDTH
            print(self.BOARD_LINER)
            print(self.BOARD_SPACE)
            print(self.BOARD_MARKS.format(
                self.positions[position_idx].position_display,
                self.positions[position_idx + 1].position_display,
                self.positions[position_idx + 2].position_display
                ))
            print(self.BOARD_SPACE)
        print(self.BOARD_LINER)

    def get_available_corner_positions(self):
        """
        Return a list of the corner positions.
        """
        corners_found = []
        for position in self.positions:
            if position.is_available_corner():
                corners_found.append(position)
        return corners_found

    def get_available_positions(self):
        """
        Return True if there are available positions.
        """
        available_positions = []
        for position in self.positions:
            if position.is_available():
                available_positions.append(position)
        return available_positions

    def get_center_position(self):
        """
        Get the middle position.  It is the best position to select for
        the turn.
        """
        center_position_idx = int((len(self.positions) - 1) / 2)
        return self.positions[center_position_idx]

    def get_stripes_with_available_positions(self):
        """
        Get a list of stripes with available positions.
        """
        stripes_found = []
        for stripe in self.stripes:
            if stripe.has_available_position():
                stripes_found.append(stripe)
        return stripes_found

    def get_stripes_with_n_player_marks(self, player, n_marks, turn_count):
        """
        Get a list of stripes with the required number of player marks.
        Skip stripes that have any marks by the other player since they
        are not winnable.
        """
        stripes_found = []
        corners_only = True if n_marks == 1 and turn_count <= 6 else False
        for stripe in self.stripes:
            if corners_only and not stripe.has_corner_positions():
                # Ignore stripes without corner positions.
                continue
            if stripe.has_n_player_marks(player, n_marks):
                stripes_found.append(stripe)
        return stripes_found

    def has_available_positions(self):
        """
        Return True if there are available positions.
        """
        for position in self.positions:
            if position.is_available():
                # The game continues.
                return True
        return False

    def is_game_over(self, player):
        """
        If a player has marked all positions in a stripe, the game is
        over; return True.
        """
        for stripe in self.stripes:
            if stripe.has_n_player_marks(player, n_marks=3):
                # The game is finished.
                return True
        return False

    def request_next_move(self):
        """
        Request the human player's move.
        """
        valid_move = False
        while not valid_move:
            player_move = input("Enter your move: ")

            if not self.valid_players_move(player_move):
                # Validate player's input.
                print("Not recognized, try again")
                continue

            selected_position_idx = int(player_move) - 1
            if not self.positions[selected_position_idx].is_available():
                # Validate selection of an available position.
                print("Already marked, try again")
                continue

            # Position selection validated.
            valid_move = True

        return self.positions[selected_position_idx]

    @staticmethod
    def valid_players_move(player_move):
        """
        Validate that the player picked an available position that is on
        the board.
        """
        return player_move.isdigit() and 1 <= int(player_move) <= 9
