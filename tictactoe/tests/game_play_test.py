#!/usr/bin/env python3
"""
Project: TicTacToe - class exercise, OOPs version
"""
from IPython.utils.capture import capture_output
from tictactoe.classes.game_play import GamePlay

class GamePlayTest:
    """
    Game play test harness.
    """
    test_game = GamePlay()

    def init_test(self):
        """
        Unit test
        """
        assert self.test_game.current_player_idx == 0
        assert self.test_game.players[0].mark == self.test_game.PLAYER_MARKS[0]
        assert self.test_game.players[1].mark == self.test_game.PLAYER_MARKS[1]

    def end_game_test(self):
        """
        Unit test
        """
        # Test game ending in a tie.
        with capture_output() as captured:
            self.test_game.end_game(None)
        captured()
        assert "Game over, tie!" in captured.stdout

        # Test the computer player winning.
        computer_player = self.test_game.players[0]
        with capture_output() as captured:
            self.test_game.end_game(computer_player)
        captured()
        assert "Game over, the compute won" in captured.stdout

        # Test the human player winning.
        human_player = self.test_game.players[1]
        with capture_output() as captured:
            self.test_game.end_game(human_player)
        captured()
        assert "Game over, you won!" in captured.stdout

    def get_next_player_test(self):
        """
        Unit test
        """
        assert self.test_game.current_player_idx == 0
        next_player = self.test_game.get_next_player()
        assert next_player.mark == 'O'
        first_player = self.test_game.get_next_player()
        assert first_player.mark == 'X'

    @staticmethod
    def take_turns_return_winner_test():
        """
        Unit test
        """
        # Test by making both players the computer since we need to fake
        # human input in order to test.
        computer_only_game = GamePlay()
        computer_only_game.players[1].is_computer = True
        computer_only_game.take_turns_return_winner()

        available_positions = computer_only_game.game_board.get_available_positions()
        if available_positions:
            # Available positions indicates a player won.
            game = computer_only_game.game_board
            first_player_won = game.is_game_over(computer_only_game.players[0])
            other_player_won = game.is_game_over(computer_only_game.players[1])
            assert first_player_won or other_player_won is True
        else:
            # No available positions indicates a tied game which
            # indicates game ran successfully.
            assert True
