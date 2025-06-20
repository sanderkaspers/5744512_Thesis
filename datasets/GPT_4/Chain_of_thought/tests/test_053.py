import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_053 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count([True, False, True, False]), 2)

    def test_all_true(self):
        self.assertEqual(count([True, True, True, True]), 4)

    def test_all_false(self):
        self.assertEqual(count([False, False, False]), 0)

    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_non_boolean_values(self):
        self.assertEqual(count([1, 0, 'True', 'False']), 0)

    def test_single_true(self):
        self.assertEqual(count([True]), 1)

    def test_mixed_data_types(self):
        self.assertEqual(count([True, False, 1, 'True']), 1)

    def test_duplicates(self):
        self.assertEqual(count([True, True, False, True, False]), 3)

    def test_nested_lists(self):
        self.assertEqual(count([[True, False], [True], False]), 0)

    def test_large_list(self):
        self.assertEqual(count([True] * 10000 + [False] * 10000), 10000)

