import unittest
from datasets.o3.programs.program_072 import *

class TestVersion(unittest.TestCase):
    def test_unique_max_occurrence(self):
        nums = [1,2,2,3,3,3,4]
        self.assertEqual(max_occurrences(nums), 3)

    def test_negative_numbers(self):
        nums = [-1, -1, 0, 2]
        self.assertEqual(max_occurrences(nums), -1)

    def test_empty_list_raises(self):
        with self.assertRaises(ValueError):
            max_occurrences([])

    def test_tie_returns_any_max(self):
        nums = [1,2,1,2]
        self.assertIn(max_occurrences(nums), {1,2})

    def test_string_list(self):
        words = ['apple','banana','apple','cherry']
        self.assertEqual(max_occurrences(words), 'apple')

