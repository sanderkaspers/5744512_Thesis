import unittest
from datasets.GPT_4.Zero_shot.programs.program_026 import *

class TestVersion(unittest.TestCase):
    def test_write_all_the__cases_for_this__to_find(self):
        test_list = [(10, 20), (30, 40), (15, 25)]
        K = 5
        expected_output = [(10, 20), (30, 40), (15, 25)]
        assert find_tuples(test_list, K) == expected_output

    def test_multiple_spaces_2(self):
        test_list = [(10, 20), (30, 40), (15, 25)]
        K = 7
        expected_output = []
        assert find_tuples(test_list, K) == expected_output

    def test_multiple_spaces_3(self):
        test_list = []
        K = 3
        expected_output = []
        assert find_tuples(test_list, K) == expected_output

    def test_multiple_spaces_4(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        K = 1
        expected_output = [(1, 2), (3, 4), (5, 6)]
        assert find_tuples(test_list, K) == expected_output

    def test_multiple_spaces_5(self):
        test_list = [(10, -20), (30, -40), (-15, 25)]
        K = -5
        expected_output = [(10, -20), (30, -40), (-15, 25)]
        assert find_tuples(test_list, K) == expected_output

    def test_multiple_spaces_6(self):
        test_list = [(0, 10), (20, 30), (40, 0)]
        K = 10
        expected_output = [(0, 10), (20, 30), (40, 0)]
        assert find_tuples(test_list, K) == expected_output

    def test_multiple_spaces_7(self):
        test_list = [(10, -20), (30, 50), (-15, 25)]
        K = 5
        expected_output = [(10, -20), (30, 50), (-15, 25)]
        assert find_tuples(test_list, K) == expected_output

