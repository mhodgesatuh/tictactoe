#!/usr/bin/env python3
#pylint: disable=import-error
"""
Project: TicTacToe - class exercise, OOPs version
"""
from tictactoe.classes.game_play import GamePlay

class SmartMoveCalculatorTest:
    """
    SmartMoveCalculater test harness.
    """

    @staticmethod
    def move_1_test():
        """
        Move 1, player X should return the center.
        """
        test_game = GamePlay()

        # Set of the board for the test.
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]
        center_position = test_game.board.get_center_position()

        # Test move 1: check that the center position is returned.
        test_turn_count = 1
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_x,
            test_player_o,
            test_turn_count)
        assert selected_position.position_idx == center_position.position_idx

    @staticmethod
    def move_2_test():
        """
        Move 2, player O should return a corner.
        """
        test_game = GamePlay()

        # Set of the board for the test.
        # Move 1: player X marks the center position.
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Set up move 1.
        test_game.board.positions[4].set_marked_by(test_player_x)

        # Test move 2: check that all of the valid corner positions are
        # randomly returned.
        test_turn_count = 2
        valid_position_idxs = [0, 2, 6, 8]
        valid_positions_idxs_found = []
        for _ in range(20):
            selected_position = test_game.move_calculator.calculate_move_for(
                test_player_o,
                test_player_x,
                test_turn_count)
            if selected_position.position_idx in valid_position_idxs and not\
                    selected_position.position_idx in valid_positions_idxs_found:
                valid_positions_idxs_found.append(selected_position.position_idx)
            if len(valid_positions_idxs_found) == len(valid_position_idxs):
                break
        assert len(valid_positions_idxs_found) == len(valid_position_idxs)

    @staticmethod
    def move_3_test():
        """
        Move 3, player X should return a corner on a stripe not marked
        by player "O".
        """
        test_game = GamePlay()
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Set up moves 1 & 2.
        test_game.board.positions[4].set_marked_by(test_player_x)
        test_game.board.positions[0].set_marked_by(test_player_o)

        # Test move 3: check that all of the valid corner positions are
        # randomly returned.
        test_turn_count = 3
        valid_position_idxs = [2, 6]
        valid_positions_idxs_found = []
        for _ in range(20):
            selected_position = test_game.move_calculator.calculate_move_for(
                test_player_x,
                test_player_o,
                test_turn_count)
            if selected_position.position_idx in valid_position_idxs and not\
                    selected_position.position_idx in valid_positions_idxs_found:
                valid_positions_idxs_found.append(selected_position.position_idx)
            if len(valid_positions_idxs_found) == len(valid_position_idxs):
                break
        assert len(valid_positions_idxs_found) == len(valid_position_idxs)

    @staticmethod
    def move_4_test():
        """
        Move 4, player O should return a corner blocking move.
        """
        test_game = GamePlay()
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Set up moves 1-3.
        #   O 2 X
        #   4 X 6
        #   7 8 9
        test_game.board.positions[4].set_marked_by(test_player_x)
        test_game.board.positions[0].set_marked_by(test_player_o)
        test_game.board.positions[2].set_marked_by(test_player_x)

        # Test move 4: check that the [3,5,7] combo is blocked.
        test_turn_count = 4
        blocking_position = test_game.board.positions[6]
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_o,
            test_player_x,
            test_turn_count)
        assert selected_position.position_idx == blocking_position.position_idx

    @staticmethod
    def move_5_test():
        """
        Move 5, player X should return a blocking move.
        """
        test_game = GamePlay()
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Set up moves 1-4.
        #   O 2 X
        #   4 X 6
        #   O 8 9
        test_game.board.positions[4].set_marked_by(test_player_x)
        test_game.board.positions[0].set_marked_by(test_player_o)
        test_game.board.positions[2].set_marked_by(test_player_x)
        test_game.board.positions[6].set_marked_by(test_player_o)

        # Test move 5: check that the [3,5,7] combo is blocked.
        test_turn_count = 5
        blocking_position = test_game.board.positions[3]
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_x,
            test_player_o,
            test_turn_count)
        assert selected_position.position_idx == blocking_position.position_idx

    @staticmethod
    def move_6_test():
        """
        Move 6, player O should return a blocking move.
        """
        test_game = GamePlay()
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Set up moves 1-5.
        #   O 2 X
        #   X X 6
        #   O 8 9
        test_game.board.positions[4].set_marked_by(test_player_x)
        test_game.board.positions[0].set_marked_by(test_player_o)
        test_game.board.positions[2].set_marked_by(test_player_x)
        test_game.board.positions[6].set_marked_by(test_player_o)
        test_game.board.positions[3].set_marked_by(test_player_x)

        # Test move 6: check that the [4,5,6] combo is blocked.
        test_turn_count = 6
        blocking_position = test_game.board.positions[5]
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_o,
            test_player_x,
            test_turn_count)
        assert selected_position.position_idx == blocking_position.position_idx

    @staticmethod
    def move_7_test():
        """
        Move 7, player X should return a blocking move.
        """
        test_game = GamePlay()
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Set up moves 1-6.
        #   O 2 X
        #   X X O
        #   O 8 9
        test_game.board.positions[4].set_marked_by(test_player_x)
        test_game.board.positions[0].set_marked_by(test_player_o)
        test_game.board.positions[2].set_marked_by(test_player_x)
        test_game.board.positions[6].set_marked_by(test_player_o)
        test_game.board.positions[3].set_marked_by(test_player_x)
        test_game.board.positions[5].set_marked_by(test_player_o)

        # Test move 7: check that a position on [2,5,8] is selected.
        test_turn_count = 7
        valid_position_idxs = [1, 7]
        valid_positions_idxs_found = []
        for _ in range(20):
            selected_position = test_game.move_calculator.calculate_move_for(
                test_player_x,
                test_player_o,
                test_turn_count)
            if selected_position.position_idx in valid_position_idxs and not\
                    selected_position.position_idx in valid_positions_idxs_found:
                valid_positions_idxs_found.append(selected_position.position_idx)
            if len(valid_positions_idxs_found) == len(valid_position_idxs):
                break
        assert len(valid_positions_idxs_found) == len(valid_position_idxs)

    @staticmethod
    def move_8_test():
        """
        Move 8, player O should return a blocking move.
        """
        test_game = GamePlay()
        test_player_o = test_game.players[0]
        test_player_x = test_game.players[1]

        # Set up moves 1-7.
        #   O 2 X
        #   X X O
        #   O X 9
        test_game.board.positions[4].set_marked_by(test_player_x)
        test_game.board.positions[0].set_marked_by(test_player_o)
        test_game.board.positions[2].set_marked_by(test_player_x)
        test_game.board.positions[6].set_marked_by(test_player_o)
        test_game.board.positions[3].set_marked_by(test_player_x)
        test_game.board.positions[5].set_marked_by(test_player_o)
        test_game.board.positions[7].set_marked_by(test_player_x)

        # Test move 7: check that a position on [2,5,8] is selected.
        test_turn_count = 8
        blocking_position = test_game.board.positions[1]
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_o,
            test_player_x,
            test_turn_count)
        assert selected_position.position_idx == blocking_position.position_idx

    @staticmethod
    def move_9_test():
        """
        Move 8, player X just picks the remaining hopeless position.
        """
        test_game = GamePlay()
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Set up moves 1-8.
        #   O O X
        #   X X O
        #   O X 9
        test_game.board.positions[4].set_marked_by(test_player_x)
        test_game.board.positions[0].set_marked_by(test_player_o)
        test_game.board.positions[2].set_marked_by(test_player_x)
        test_game.board.positions[6].set_marked_by(test_player_o)
        test_game.board.positions[3].set_marked_by(test_player_x)
        test_game.board.positions[5].set_marked_by(test_player_o)
        test_game.board.positions[7].set_marked_by(test_player_x)
        test_game.board.positions[1].set_marked_by(test_player_o)

        # Test move 7: check that the remaining position is selected.
        test_turn_count = 9
        blocking_position = test_game.board.positions[8]
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_o,
            test_player_x,
            test_turn_count)
        assert selected_position.position_idx == blocking_position.position_idx
