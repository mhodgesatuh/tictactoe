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

    TEST_ITERATIONS = 20

    @staticmethod
    def _setup_game_up_to_move(move_cnt):
        """
        Mark the positions up to the move count in order to set the test
        scenario.
        """
        test_game = GamePlay()
        move_sequence = [4, 0, 2, 6, 3, 5, 7, 1]
        for idx in range(move_cnt):
            position_idx = move_sequence[idx]
            player = test_game.get_current_player()
            test_game.board.positions[position_idx].set_marked_by(player)
            test_game.turn_count += 1
        return test_game

    @staticmethod
    def move_1_test():
        """
        Move 1, player X should return the center.
        """
        test_game = GamePlay()
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Test move 1: check that the center position is returned.
        test_turn_count = 1
        center_position = test_game.board.get_center_position()
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_x,
            test_player_o,
            test_turn_count)

        assert selected_position.position_idx == center_position.position_idx

    def move_2_test(self):
        """
        Move 2, player O should return a corner.
        Setup:
            1 2 3
            4 X 6
            7 8 9
        """
        test_game = self._setup_game_up_to_move(1)

        # Set of the board for the test.
        # Move 1: player X marks the center position.
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Test move 2: check that all of the valid corner positions are
        # randomly returned.
        test_turn_count = 2
        valid_position_idxs = [0, 2, 6, 8]
        valid_positions_idxs_found = []

        # Rerun the test multiple times in order to see all of the
        # possible random selections.
        for _ in range(self.TEST_ITERATIONS):
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

    def move_3_test(self):
        """
        Move 3, player X should return a corner on a stripe not marked
        by player "O".
        Setup:
            O 2 3
            4 X 6
            7 8 9
        """
        test_game = self._setup_game_up_to_move(2)
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Test move 3: check that all of the valid corner positions are
        # randomly returned.
        test_turn_count = 3
        valid_position_idxs = [2, 6]
        valid_positions_idxs_found = []

        # Rerun the test multiple times in order to see all of the
        # possible random selections.
        for _ in range(self.TEST_ITERATIONS):
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

    def move_4_test(self):
        """
        Move 4, player O should return a corner blocking move.
        Setup:
            O 2 X
            4 X 6
            7 8 9
        """
        test_game = self._setup_game_up_to_move(3)
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Test move 4: check that the [3,5,7] combo is blocked.
        test_turn_count = 4
        blocking_position = test_game.board.positions[6]
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_o,
            test_player_x,
            test_turn_count)

        assert selected_position.position_idx == blocking_position.position_idx

    def move_5_test(self):
        """
        Move 5, player X should return a blocking move.
        Setup:
            O 2 X
            4 X 6
            O 8 9
        """
        test_game = self._setup_game_up_to_move(4)
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Test move 5: check that the [3,5,7] combo is blocked.
        test_turn_count = 5
        blocking_position = test_game.board.positions[3]
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_x,
            test_player_o,
            test_turn_count)

        assert selected_position.position_idx == blocking_position.position_idx

    def move_6_test(self):
        """
        Move 6, player O should return a blocking move.
        Setup:
            O 2 X
            X X 6
            O 8 9
        """
        test_game = self._setup_game_up_to_move(5)
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Test move 6: check that the [4,5,6] combo is blocked.
        test_turn_count = 6
        blocking_position = test_game.board.positions[5]
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_o,
            test_player_x,
            test_turn_count)

        assert selected_position.position_idx == blocking_position.position_idx

    def move_7_test(self):
        """
        Move 7, player X should return a blocking move.
        Setup:
            O 2 X
            X X O
            O 8 9
        """
        test_game = self._setup_game_up_to_move(6)
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Test move 7: check that a position on [2,5,8] is selected.
        test_turn_count = 7
        valid_position_idxs = [1, 7]
        valid_positions_idxs_found = []

        # Rerun the test multiple times in order to see all of the
        # possible random selections.
        for _ in range(self.TEST_ITERATIONS):
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

    def move_8_test(self):
        """
        Move 8, player O should return a blocking move.
        Setup:
            O 2 X
            X X O
            O X 9
        """
        test_game = self._setup_game_up_to_move(7)
        test_player_o = test_game.players[0]
        test_player_x = test_game.players[1]

        # Test move 7: check that a position on [2,5,8] is selected.
        test_turn_count = 8
        blocking_position = test_game.board.positions[1]
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_o,
            test_player_x,
            test_turn_count)

        assert selected_position.position_idx == blocking_position.position_idx

    def move_9_test(self):
        """
        Move 8, player X just picks the remaining hopeless position.
        Setup:
            O O X
            X X O
            O X 9
        """
        test_game = self._setup_game_up_to_move(8)
        test_player_x = test_game.players[0]
        test_player_o = test_game.players[1]

        # Test move 7: check that the remaining position is selected.
        test_turn_count = 9
        blocking_position = test_game.board.positions[8]
        selected_position = test_game.move_calculator.calculate_move_for(
            test_player_o,
            test_player_x,
            test_turn_count)

        assert selected_position.position_idx == blocking_position.position_idx
