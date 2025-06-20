import unittest
from datasets.GPT_4.Zero_shot.programs.program_025 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        colors = ['red', 'blue', 'red', 'blue']
        patterns = ['A', 'B', 'A', 'B']
        expected_output = True
        assert is_samepatterns(colors, patterns) == expected_output

    def test_multiple_spaces_2(self):
        colors = ['red', 'blue', 'blue', 'red']
        patterns = ['A', 'B', 'A', 'B']
        expected_output = False
        assert is_samepatterns(colors, patterns) == expected_output

    def test_multiple_spaces_3(self):
        colors = []
        patterns = ['A', 'B']
        expected_output = False
        assert is_samepatterns(colors, patterns) == expected_output

    def test_multiple_spaces_4(self):
        colors = ['red', 'blue']
        patterns = []
        expected_output = False
        assert is_samepatterns(colors, patterns) == expected_output

    def test_multiple_spaces_5(self):
        colors = []
        patterns = []
        expected_output = True
        assert is_samepatterns(colors, patterns) == expected_output

    def test_multiple_spaces_6(self):
        colors = ['red']
        patterns = ['A']
        expected_output = True
        assert is_samepatterns(colors, patterns) == expected_output

    def test_multiple_spaces_7(self):
        colors = ['red', 'red', 'red']
        patterns = ['A', 'A', 'A']
        expected_output = True
        assert is_samepatterns(colors, patterns) == expected_output

    def test_multiple_spaces_8(self):
        colors = ['red', 'blue', 'green']
        patterns = ['A', 'A', 'A']
        expected_output = False
        assert is_samepatterns(colors, patterns) == expected_output

    def test_multiple_spaces_9(self):
        colors = ['red', 'blue', 'green', 'red', 'blue', 'green']
        patterns = ['A', 'B', 'C', 'A', 'B', 'C']
        expected_output = True
        assert is_samepatterns(colors, patterns) == expected_output

