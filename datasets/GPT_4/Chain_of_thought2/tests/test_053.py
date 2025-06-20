import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_053 import *

class TestVersion(unittest.TestCase):
    def test_all_true(self): self.assertEqual(count([True, True, True]), 3)

    def test_all_false(self): self.assertEqual(count([False, False]), 0)

    def test_mixed_true_false(self): self.assertEqual(count([True, False, True, False]), 2)

    def test_empty_list(self): self.assertEqual(count([]), 0)

    def test_single_true(self): self.assertEqual(count([True]), 1)

    def test_single_false(self): self.assertEqual(count([False]), 0)

    def test_non_boolean_values(self): self.assertEqual(count([1, 0, True, False]), 2)

    def test_string_and_none_values(self): self.assertEqual(count(['', 'yes', True, None]), 2)

    def test_all_falsy_values(self): self.assertEqual(count([False, None, 0, '', [], {}]), 0)

