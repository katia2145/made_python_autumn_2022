import unittest
import numpy as np
import sys
from io import StringIO

from TicTacGame import TicTacGame


class TestTicTacGame(unittest.TestCase):
    def fill_row(self, arr, row, cur_char):
        for i in range(len(arr)):
            arr[row][i] = cur_char
        return arr

    def test_finish_game(self):
        game = TicTacGame()
        start_board = np.array([
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."]])

        game.board = start_board
        result = game.check_finish_game()
        self.assertEqual(result, "continue game")

        # проверяем выйгрыш по строке
        game.board = self.fill_row(start_board, 0, "o")
        result = game.check_finish_game()
        self.assertEqual(result, "o win")

        game.board = self.fill_row(start_board, 1, "o")
        result = game.check_finish_game()
        self.assertEqual(result, "o win")

        game.board = self.fill_row(start_board, 2, "o")
        result = game.check_finish_game()
        self.assertEqual(result, "o win")

        game.board = self.fill_row(start_board, 0, "x")
        result = game.check_finish_game()
        self.assertEqual(result, "x win")

        game.board = self.fill_row(start_board, 1, "x")
        result = game.check_finish_game()
        self.assertEqual(result, "x win")

        game.board = self.fill_row(start_board, 2, "x")
        result = game.check_finish_game()
        self.assertEqual(result, "x win")

        game.board = np.array([
            ["o", ".", "o"],
            [".", ".", "."],
            [".", "x", "."]])

        result = game.check_finish_game()
        self.assertEqual(result, "continue game")

        game.board = np.array([
            [".", ".", "."],
            ["o", "x", "o"],
            [".", ".", "."]])

        result = game.check_finish_game()
        self.assertEqual(result, "continue game")

        game.board = np.array([
            ["x", ".", "x"],
            ["o", "x", "o"],
            [".", "o", "."]])

        result = game.check_finish_game()
        self.assertEqual(result, "continue game")

        # проверяем диагонали
        game.board = np.array([
            [".", ".", "o"],
            [".", "x", "."],
            ["o", ".", "."]])

        result = game.check_finish_game()
        self.assertEqual(result, "continue game")

        game.board = np.array([
            [".", ".", "o"],
            [".", "o", "."],
            ["o", ".", "."]])

        result = game.check_finish_game()
        self.assertEqual(result, "o win")

        game.board = np.array([
            [".", ".", "x"],
            [".", "x", "."],
            ["x", ".", "."]])

        result = game.check_finish_game()
        self.assertEqual(result, "x win")

        game.board = np.array([
            ["x", ".", "."],
            [".", "x", "."],
            [".", ".", "x"]])

        result = game.check_finish_game()
        self.assertEqual(result, "x win")

        game.board = np.array([
            ["o", ".", "."],
            [".", "o", "."],
            [".", ".", "o"]])

        result = game.check_finish_game()
        self.assertEqual(result, "o win")

        game.board = np.array([
            ["o", ".", "."],
            [".", "o", "."],
            [".", ".", "x"]])

        result = game.check_finish_game()
        self.assertEqual(result, "continue game")

        game.board = np.array([
            ["o", ".", "o"],
            [".", "o", "x"],
            ["x", ".", "x"]])

        result = game.check_finish_game()
        self.assertEqual(result, "continue game")

        # проверяем ничью
        game.board = np.array([
            ["o", "o", "x"],
            ["x", "o", "o"],
            ["o", "x", "x"]])

        result = game.check_finish_game()
        self.assertEqual(result, "dead heat")

    def test_validate_input(self):
        self.stub_stdouts(self)

        game = TicTacGame()

        result = game.validate_input("12 2")
        self.assertEqual(result, False)

        result = game.validate_input("0 2")
        self.assertEqual(result, False)

        result = game.validate_input("2 4")
        self.assertEqual(result, False)

        result = game.validate_input("-1 3")
        self.assertEqual(result, False)

        result = game.validate_input("asdf 2")
        self.assertEqual(result, False)

        result = game.validate_input("1 asdf")
        self.assertEqual(result, False)

        result = game.validate_input("asd")
        self.assertEqual(result, False)

        result = game.validate_input("2")
        self.assertEqual(result, False)

        result = game.validate_input("1 2 3")
        self.assertEqual(result, False)

        result = game.validate_input("1, 2")
        self.assertEqual(result, False)

        result = game.validate_input("#1 *2")
        self.assertEqual(result, False)

        result = game.validate_input("1.4 2.0")
        self.assertEqual(result, False)

        result = game.validate_input("0.5")
        self.assertEqual(result, False)

        result = game.validate_input("1 1")
        self.assertEqual(result, True)

        result = game.validate_input("1 3")
        self.assertEqual(result, True)

        result = game.validate_input("3 3")
        self.assertEqual(result, True)

    def test_make_step_on_board(self):
        self.stub_stdouts(self)
        game = TicTacGame()

        result = game.validate_input("2 2")
        self.assertEqual(result, True)

        game.make_step_on_board("2 2", "x")
        true_board = np.array([
            [".", ".", "."],
            [".", "x", "."],
            [".", ".", "."]]).tolist()
        self.assertListEqual(game.board.tolist(), true_board)

        result = game.validate_input("2 2")
        self.assertEqual(result, False)

        result = game.validate_input("1 2")
        self.assertEqual(result, True)

        game.make_step_on_board("1 2", "o")
        true_board = np.array([
            [".", "o", "."],
            [".", "x", "."],
            [".", ".", "."]]).tolist()
        self.assertEqual(game.board.tolist(), true_board)

    # def stub_stdin(self, testcase_inst, inputs):
    #     stdin = sys.stdin

    #     def cleanup():
    #         sys.stdin = stdin

    #     testcase_inst.addCleanup(cleanup)
    #     sys.stdin = StringIO(inputs)

    def stub_stdouts(self, testcase_inst):
        stdout = sys.stdout

        def cleanup():
            sys.stdout = stdout

        testcase_inst.addCleanup(cleanup)
        sys.stdout = StringIO()


if __name__ == "__main__":
    unittest.main()
