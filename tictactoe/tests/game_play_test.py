#!/usr/bin/env python3
#pylint: disable=import-error
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

    def get_current_player_test(self):
        """
        Unit test.
        """
        self.test_game.turn_count = 1
        current_player = self.test_game.get_current_player()
        assert current_player.mark == self.test_game.PLAYER_MARKS[0]

    def get_next_player_test(self):
        """
        Unit test
        """
        self.test_game.turn_count = 1
        current_player = self.test_game.get_current_player()
        next_player = self.test_game.get_next_player()
        assert next_player.mark == self.test_game.PLAYER_MARKS[1]
        assert not current_player.mark == next_player.mark

    @staticmethod
    def take_turns_return_winner_test():
        """
        Unit test
        """
        # Test by making both players the computer since we need to fake
        # human input in order to test.
        computer_only_game = GamePlay()
        computer_only_game.players[1].computer_player = True
        # Computer players should play to a draw every time.
        assert computer_only_game.take_turns_return_winner() is None
        assert not computer_only_game.board.has_available_positions()
