import unittest
from datasets.GPT_4.Chain_of_thought.programs.program_043 import *

class TestVersion(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Find_Min_Length([[1, 2, 3], [1, 2], [1]]), 1)

    def test_single_list(self):
        self.assertEqual(Find_Min_Length([[1, 2, 3]]), 3)

    def test_empty_list_of_lists(self):
        with self.assertRaises(ValueError):
            Find_Min_Length([])

    def test_sublist_with_zero_length(self):
        self.assertEqual(Find_Min_Length([[1, 2, 3], [], [1, 2]]), 0)

    def test_all_same_length(self):
        self.assertEqual(Find_Min_Length([[1, 2], [3, 4], [5, 6]]), 2)

    def test_nested_empty_sublists(self):
        self.assertEqual(Find_Min_Length([[], [], []]), 0)

    def test_large_sublists(self):
        large_list = [[i for i in range(1000)], [j for j in range(500)], [k for k in range(2000)]]
        self.assertEqual(Find_Min_Length(large_list), 500)

    def test_mixed_data_types(self):
        self.assertEqual(Find_Min_Length([[1, 'a', 3.5], [1, 2], ['a']]), 1)

    def test_sublists_with_structures(self):
        self.assertEqual(Find_Min_Length([[1, 2], {'key': 'value'}, (1, 2, 3)]), 2)

