import unittest
import logic

class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', ' ', '0'],
            [' ', 'X', ' '],
            [' ', 'O', 'X']
        ]
        self.assertEqual(logic.check_diagonal(board), 'X')

    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()