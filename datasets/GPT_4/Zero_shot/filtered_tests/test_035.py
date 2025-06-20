import unittest
from datasets.GPT_4.Zero_shot.programs.program_035 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        dict3 = {'c': 3}
        expected_output = {'a': 1, 'b': 2, 'c': 3}
        assert merge_dictionaries_three(dict1, dict2, dict3) == expected_output

    def test_multiple_spaces_2(self):
        dict1 = {}
        dict2 = {}
        dict3 = {}
        expected_output = {}
        assert merge_dictionaries_three(dict1, dict2, dict3) == expected_output

    def test_multiple_spaces_3(self):
        dict1 = {}
        dict2 = {'b': 2}
        dict3 = {}
        expected_output = {'b': 2}
        assert merge_dictionaries_three(dict1, dict2, dict3) == expected_output

    def test_multiple_spaces_4(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'c': 5, 'd': 6}
        expected_output = {'a': 1, 'b': 2, 'c': 4, 'd': 6}
        assert merge_dictionaries_three(dict1, dict2, dict3) == expected_output

    def test_multiple_spaces_5(self):
        dict1 = {'a': None}
        dict2 = {'b': None}
        dict3 = {'c': None}
        expected_output = {'a': None, 'b': None, 'c': None}
        assert merge_dictionaries_three(dict1, dict2, dict3) == expected_output

    def test_multiple_spaces_6(self):
        dict1 = {'a': 1}
        dict2 = {'b': 'string'}
        dict3 = {'c': [1, 2, 3]}
        expected_output = {'a': 1, 'b': 'string', 'c': [1, 2, 3]}
        assert merge_dictionaries_three(dict1, dict2, dict3) == expected_output

    def test_multiple_spaces_7(self):
        dict1 = {'a': {'x': 1}}
        dict2 = {'b': {'y': 2}}
        dict3 = {'c': {'z': 3}}
        expected_output = {'a': {'x': 1}, 'b': {'y': 2}, 'c': {'z': 3}}
        assert merge_dictionaries_three(dict1, dict2, dict3) == expected_output

