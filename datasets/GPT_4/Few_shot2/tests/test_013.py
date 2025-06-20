import unittest
from datasets.GPT_4.Few_shot2.programs.program_013 import *

class TestVersion(unittest.TestCase):
    def test_count_Occurrence_basic(self): self.assertEqual(count_Occurrence([1, 2, 2, 3]), {1: 1, 2: 2, 3: 1})

    def test_count_Occurrence_empty(self): self.assertEqual(count_Occurrence([]), {})

    def test_count_Occurrence_all_same(self): self.assertEqual(count_Occurrence([5, 5, 5]), {5: 3})

    def test_count_Occurrence_all_unique(self): self.assertEqual(count_Occurrence([1, 2, 3]), {1: 1, 2: 1, 3: 1})

    def test_count_Occurrence_strings(self): self.assertEqual(count_Occurrence(['a', 'b', 'a']), {'a': 2, 'b': 1})

    def test_count_Occurrence_mixed_types(self): self.assertEqual(count_Occurrence([1, '1', 1]), {1: 2, '1': 1})

    def test_count_Occurrence_with_none(self): self.assertEqual(count_Occurrence([None, None, 1]), {None: 2, 1: 1})

    def test_count_Occurrence_large_input(self): self.assertEqual(count_Occurrence([1]*1000 + [2]*500), {1: 1000, 2: 500})

