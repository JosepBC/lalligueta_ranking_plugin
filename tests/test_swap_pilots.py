import unittest
from swap_pilots import swap_on_grouped_board
import logging

logger = logging.getLogger(__name__)

class TestSwapPilots(unittest.TestCase):
    def test_multiple_of_five(self):
        init_board = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'D', 'heat': 'H1', 'heat_rank': 4}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': 5}],
                      [{'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'I', 'heat': 'H2', 'heat_rank': 4}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': 5}],
                      [{'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'N', 'heat': 'H3', 'heat_rank': 4}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': 5}],
                      [{'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}, {'callsign': 'R', 'heat': 'H4', 'heat_rank': 3}, {'callsign': 'S', 'heat': 'H4', 'heat_rank': 4}, {'callsign': 'T', 'heat': 'H4', 'heat_rank': 5}],
                      [{'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': 3}, {'callsign': 'X', 'heat': 'H5', 'heat_rank': 4}, {'callsign': 'Y', 'heat': 'H5', 'heat_rank': 5}]]

        result = swap_on_grouped_board(init_board, logger)

        expected_result = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}],
                           [{'callsign': 'D', 'heat': 'H1', 'heat_rank': 4}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': 5}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}],
                           [{'callsign': 'I', 'heat': 'H2', 'heat_rank': 4}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': 5}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}],
                           [{'callsign': 'N', 'heat': 'H3', 'heat_rank': 4}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': 5}, {'callsign': 'R', 'heat': 'H4', 'heat_rank': 3}, {'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}],
                           [{'callsign': 'S', 'heat': 'H4', 'heat_rank': 4}, {'callsign': 'T', 'heat': 'H4', 'heat_rank': 5}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': 3}, {'callsign': 'X', 'heat': 'H5', 'heat_rank': 4}, {'callsign': 'Y', 'heat': 'H5', 'heat_rank': 5}]]

        self.assertEqual(result, expected_result)

    def test_minus_four(self):
        init_board = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'D', 'heat': 'H1', 'heat_rank': 4}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': 5}],
                      [{'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'I', 'heat': 'H2', 'heat_rank': 4}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': 5}],
                      [{'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'N', 'heat': 'H3', 'heat_rank': 4}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': 5}],
                      [{'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}, {'callsign': 'R', 'heat': 'H4', 'heat_rank': 3}],
                      [{'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': 3}]]

        result = swap_on_grouped_board(init_board, logger)

        expected_result = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}],
                           [{'callsign': 'D', 'heat': 'H1', 'heat_rank': 4}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': 5}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}],
                           [{'callsign': 'I', 'heat': 'H2', 'heat_rank': 4}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': 5}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}],
                           [{'callsign': 'N', 'heat': 'H3', 'heat_rank': 4}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': 5}, {'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}],
                           [{'callsign': 'R', 'heat': 'H4', 'heat_rank': 3}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': 3}]]

        self.assertEqual(result, expected_result)


    def test_minus_three(self):
        init_board = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'D', 'heat': 'H1', 'heat_rank': 4}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': 5}],
                      [{'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'I', 'heat': 'H2', 'heat_rank': 4}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': 5}],
                      [{'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'N', 'heat': 'H3', 'heat_rank': 4}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': 5}],
                      [{'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}, {'callsign': 'R', 'heat': 'H4', 'heat_rank': 3}, {'callsign': 'S', 'heat': 'H4', 'heat_rank': 4}],
                      [{'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': 3}]]

        result = swap_on_grouped_board(init_board, logger)

        expected_result = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}],
                           [{'callsign': 'D', 'heat': 'H1', 'heat_rank': 4}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': 5}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}],
                           [{'callsign': 'I', 'heat': 'H2', 'heat_rank': 4}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': 5}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}],
                           [{'callsign': 'N', 'heat': 'H3', 'heat_rank': 4}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': 5}, {'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}],
                           [{'callsign': 'R', 'heat': 'H4', 'heat_rank': 3}, {'callsign': 'S', 'heat': 'H4', 'heat_rank': 4}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': 3}]]

        self.assertEqual(result, expected_result)

    def test_minus_two(self):
        init_board = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'D', 'heat': 'H1', 'heat_rank': 4}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': 5}],
                      [{'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'I', 'heat': 'H2', 'heat_rank': 4}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': 5}],
                      [{'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'N', 'heat': 'H3', 'heat_rank': 4}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': 5}],
                      [{'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}, {'callsign': 'R', 'heat': 'H4', 'heat_rank': 3}, {'callsign': 'S', 'heat': 'H4', 'heat_rank': 4}],
                      [{'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': 3}, {'callsign': 'X', 'heat': 'H5', 'heat_rank': 4}]]

        result = swap_on_grouped_board(init_board, logger)

        expected_result = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}],
                           [{'callsign': 'D', 'heat': 'H1', 'heat_rank': 4}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': 5}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}],
                           [{'callsign': 'I', 'heat': 'H2', 'heat_rank': 4}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': 5}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}],
                           [{'callsign': 'N', 'heat': 'H3', 'heat_rank': 4}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': 5}, {'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}],
                           [{'callsign': 'R', 'heat': 'H4', 'heat_rank': 3}, {'callsign': 'S', 'heat': 'H4', 'heat_rank': 4}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': 3}, {'callsign': 'X', 'heat': 'H5', 'heat_rank': 4}]]

        self.assertEqual(result, expected_result)

    def test_minus_one(self):
        init_board = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'D', 'heat': 'H1', 'heat_rank': 4}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': 5}],
                      [{'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'I', 'heat': 'H2', 'heat_rank': 4}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': 5}],
                      [{'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'N', 'heat': 'H3', 'heat_rank': 4}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': 5}],
                      [{'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}, {'callsign': 'R', 'heat': 'H4', 'heat_rank': 3}, {'callsign': 'S', 'heat': 'H4', 'heat_rank': 4}, {'callsign': 'T', 'heat': 'H4', 'heat_rank': 5}],
                      [{'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': 3}, {'callsign': 'X', 'heat': 'H5', 'heat_rank': 4}]]

        result = swap_on_grouped_board(init_board, logger)

        expected_result = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}],
                           [{'callsign': 'D', 'heat': 'H1', 'heat_rank': 4}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': 5}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}],
                           [{'callsign': 'I', 'heat': 'H2', 'heat_rank': 4}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': 5}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}],
                           [{'callsign': 'N', 'heat': 'H3', 'heat_rank': 4}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': 5}, {'callsign': 'R', 'heat': 'H4', 'heat_rank': 3}, {'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}],
                           [{'callsign': 'S', 'heat': 'H4', 'heat_rank': 4}, {'callsign': 'T', 'heat': 'H4', 'heat_rank': 5}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': 3}, {'callsign': 'X', 'heat': 'H5', 'heat_rank': 4}]]

        self.assertEqual(result, expected_result)

    def test_minus_3_max_pilots_no_lap_per_group(self):
        # Heat rank is None if pilot hasn't done a singe pass on Start/Finish line
        init_board = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'D', 'heat': 'H1', 'heat_rank': None}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': None}],
                      [{'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'I', 'heat': 'H2', 'heat_rank': None}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': None}],
                      [{'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'N', 'heat': 'H3', 'heat_rank': None}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': None}],
                      [{'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}, {'callsign': 'R', 'heat': 'H4', 'heat_rank': None}, {'callsign': 'S', 'heat': 'H4', 'heat_rank': None}],
                      [{'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': None}]]

        result = swap_on_grouped_board(init_board, logger)

        expected_result = [[{'callsign': 'A', 'heat': 'H1', 'heat_rank': 1}, {'callsign': 'B', 'heat': 'H1', 'heat_rank': 2}, {'callsign': 'C', 'heat': 'H1', 'heat_rank': 3}, {'callsign': 'F', 'heat': 'H2', 'heat_rank': 1}, {'callsign': 'G', 'heat': 'H2', 'heat_rank': 2}],
                            [{'callsign': 'D', 'heat': 'H1', 'heat_rank': None}, {'callsign': 'E', 'heat': 'H1', 'heat_rank': None}, {'callsign': 'H', 'heat': 'H2', 'heat_rank': 3}, {'callsign': 'K', 'heat': 'H3', 'heat_rank': 1}, {'callsign': 'L', 'heat': 'H3', 'heat_rank': 2}],
                            [{'callsign': 'I', 'heat': 'H2', 'heat_rank': None}, {'callsign': 'J', 'heat': 'H2', 'heat_rank': None}, {'callsign': 'M', 'heat': 'H3', 'heat_rank': 3}, {'callsign': 'P', 'heat': 'H4', 'heat_rank': 1}, {'callsign': 'Q', 'heat': 'H4', 'heat_rank': 2}],
                            [{'callsign': 'N', 'heat': 'H3', 'heat_rank': None}, {'callsign': 'O', 'heat': 'H3', 'heat_rank': None}, {'callsign': 'U', 'heat': 'H5', 'heat_rank': 1}, {'callsign': 'V', 'heat': 'H5', 'heat_rank': 2}],
                            [{'callsign': 'R', 'heat': 'H4', 'heat_rank': None}, {'callsign': 'S', 'heat': 'H4', 'heat_rank': None}, {'callsign': 'W', 'heat': 'H5', 'heat_rank': None}]]

        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
