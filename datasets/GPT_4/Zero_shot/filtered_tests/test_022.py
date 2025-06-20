import unittest
from datasets.GPT_4.Zero_shot.programs.program_022 import *

class TestVersion(unittest.TestCase):
    def test_write_all_the__cases_for_this__to_find(self):
        Input = [(1, 2), (3, 4), (5, 6)]
        expected_output = True
        assert get_equal(Input) == expected_output

    def test_write_all_the__cases_for_this__to_find_1(self):
        Input = [(1, 2), (3, 4, 5), (6, 7)]
        expected_output = False
        assert get_equal(Input) == expected_output

    def test_multiple_spaces_3(self):
        Input = []
        expected_output = True
        assert get_equal(Input) == expected_output

    def test_write_all_the__cases_for_this__to_find_2(self):
        Input = [(1, 2, 3)]
        expected_output = True
        assert get_equal(Input) == expected_output

    def test_multiple_spaces_5(self):
        Input = [(1, "a"), (2, "b"), (3, "c")]
        expected_output = True
        assert get_equal(Input) == expected_output

    def test_multiple_spaces_6(self):
        Input = [(), (), ()]
        expected_output = True
        assert get_equal(Input) == expected_output

    def test_write_all_the__cases_for_this__to_find_3(self):
        Input = [(), (1,), (2, 3)]
        expected_output = False
        assert get_equal(Input) == expected_output

