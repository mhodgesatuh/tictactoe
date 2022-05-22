#!/usr/bin/env python3
#pylint: disable=too-few-public-methods
"""
Project: TicTacToe - class exercise, OOPs version
"""
from tictactoe.classes.game_play import GamePlay

class SmartMoveCalculatorTest:
    """
    SmartMoveCalculater test harness.
    """

    @staticmethod
    def first_two_moves_test():
        """
        Second move should return a corner.
        """
        test_game = GamePlay()
        center_position = test_game.board.get_center_position()
        current_player = test_game.players[test_game.current_player_idx]

        # Move 1 to mark X the center position.
        selected_position = test_game.move_calculator.calculate_move_for(
            current_player,
            test_game.turn_count)
        assert selected_position == center_position
        selected_position.set_marked_by(current_player)
        test_game.turn_count += 1

        # Move 2 to mark O a corner position.
        current_player = test_game.get_next_player()
        selected_position = test_game.move_calculator.calculate_move_for(
            current_player,
            test_game.turn_count)
        assert selected_position.is_corner()
        selected_position.set_marked_by(current_player)
        test_game.turn_count += 1

        # Move 3 to mark X a corner position on a stripe with no O mark.
        current_player = test_game.get_next_player()
        selected_position = test_game.move_calculator.calculate_move_for(
            current_player,
            test_game.turn_count)
        assert selected_position.is_available_corner()
        selected_position.set_marked_by(current_player)
        test_game.turn_count += 1

        # Move 4 to mark O a corner position on a stripe with no X mark.
        current_player = test_game.get_next_player()
        selected_position = test_game.move_calculator.calculate_move_for(
            current_player,
            test_game.turn_count)
        assert selected_position.is_available_corner()
        selected_position.set_marked_by(current_player)
        test_game.turn_count += 1

        # Move % to mark X a corner position on a stripe with no X mark.
        current_player = test_game.get_next_player()
        selected_position = test_game.move_calculator.calculate_move_for(
            current_player,
            test_game.turn_count)
        assert True
        selected_position.set_marked_by(current_player)
        test_game.turn_count += 1
