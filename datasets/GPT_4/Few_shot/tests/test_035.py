import unittest
from datasets.GPT_4.Few_shot.programs.program_035 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 5, 'c': 4}) # Overlapping keys)

    def test_case_2(self):
        self.assertEqual(merge_dictionaries_three({'a': 1}, {'b': 2}), {'a': 1, 'b': 2}) # No overlapping keys)

    def test_case_3(self):
        self.assertEqual(merge_dictionaries_three({}, {'a': 1}), {'a': 1}) # First dictionary empty)

    def test_case_4(self):
        self.assertEqual(merge_dictionaries_three({'a': 1}, {}), {'a': 1}) # Second dictionary empty)

    def test_case_5(self):
        self.assertEqual(merge_dictionaries_three({}, {}), {}) # Both dictionaries empty)

    def test_case_6(self):
        self.assertEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'a': 3, 'b': 4, 'c': 5}), {'a': 4, 'b': 6, 'c': 5}) # Multiple overlaps)

    def test_case_7(self):
        self.assertEqual(merge_dictionaries_three({'x': 10, 'y': 20}, {'y': 5, 'z': 30}), {'x': 10, 'y': 25, 'z': 30}) # Partial overlap)

    def test_case_8(self):
        self.assertEqual(merge_dictionaries_three({'large_key': 1000000000}, {'large_key': 2000000000}), {'large_key': 3000000000}) # Large numbers)

