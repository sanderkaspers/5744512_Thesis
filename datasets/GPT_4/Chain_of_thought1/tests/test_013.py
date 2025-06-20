import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_013 import *

class TestVersion(unittest.TestCase):
    def test_unique_integers(self): self.assertEqual(count_frequency([1, 2, 3]), {1: 1, 2: 1, 3: 1})

    def test_repeated_integers(self): self.assertEqual(count_frequency([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})

    def test_mixed_types(self): self.assertEqual(count_frequency([1, '1', 1.0]), {1: 2, '1': 1})

    def test_all_same_element(self): self.assertEqual(count_frequency([7, 7, 7, 7]), {7: 4})

    def test_empty_list(self): self.assertEqual(count_frequency([]), {})

    def test_strings(self): self.assertEqual(count_frequency(['apple', 'banana', 'apple']), {'apple': 2, 'banana': 1})

    def test_none_element(self): self.assertEqual(count_frequency([None, None, 'None']), {None: 2, 'None': 1})

    def test_booleans(self): self.assertEqual(count_frequency([True, False, True, 1]), {True: 3, False: 1})

    def test_large_input(self): large_input = [5]*10000 + [3]*5000; self.assertEqual(count_frequency(large_input), {5: 10000, 3: 5000})

