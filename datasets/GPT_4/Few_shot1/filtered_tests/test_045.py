import unittest
from datasets.GPT_4.Few_shot1.programs.program_045 import *

class TestVersion(unittest.TestCase):
    def test_frequency_lists_basic(self): self.assertEqual(frequency_lists([[1, 2], [2, 3]]), {1: 1, 2: 2, 3: 1})

    def test_frequency_lists_empty(self): self.assertEqual(frequency_lists([]), {})

    def test_frequency_lists_nested_empty(self): self.assertEqual(frequency_lists([[], []]), {})

    def test_frequency_lists_single_sublist(self): self.assertEqual(frequency_lists([[4, 4, 4]]), {4: 3})

    def test_frequency_lists_multiple_types(self): self.assertEqual(frequency_lists([[1, '1'], ['1', 1]]), {1: 2, '1': 2})

    def test_frequency_lists_large(self): self.assertEqual(frequency_lists([[1]*1000, [2]*500]), {1: 1000, 2: 500})

