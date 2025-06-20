import unittest
from datasets.GPT_4.Zero_shot.programs.program_059 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        list1 = [{}, {}, {}]
        expected_output = True
        assert empty_dit(list1) == expected_output

    def test_multiple_spaces_2(self):
        list1 = [{}, {"key": "value"}, {}]
        expected_output = False
        assert empty_dit(list1) == expected_output

    def test_multiple_spaces_3(self):
        list1 = [{}, {}, {"another_key": 123}]
        expected_output = False
        assert empty_dit(list1) == expected_output

    def test_multiple_spaces_4(self):
        list1 = []
        expected_output = True  # No dictionaries, so return True
        assert empty_dit(list1) == expected_output

    def test_multiple_spaces_5(self):
        list1 = [{}, [], 42, "string"]
        expected_output = False  # Non-dictionary elements should make the function return False
        assert empty_dit(list1) == expected_output

    def test_multiple_spaces_6(self):
        list1 = [{}, {"nested": {}}]
        expected_output = False  # Nested dictionary, should be treated as non-empty
        assert empty_dit(list1) == expected_output

