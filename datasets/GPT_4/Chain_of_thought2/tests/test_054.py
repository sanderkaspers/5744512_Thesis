import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_054 import *

class TestVersion(unittest.TestCase):
    def test_regular_case(self): self.assertEqual(add_lists([4, 5], (1, 2)), (1, 2, 4, 5))

    def test_empty_list(self): self.assertEqual(add_lists([], (7, 8)), (7, 8))

    def test_empty_tuple(self): self.assertEqual(add_lists([9, 10], ()), (9, 10))

    def test_both_empty(self): self.assertEqual(add_lists([], ()), ())

    def test_list_with_mixed_types(self): self.assertEqual(add_lists([True, 'str', 3.14], (1,)), (1, True, 'str', 3.14))

    def test_tuple_with_nested_structures(self): self.assertEqual(add_lists([5], ((1, 2),)), ((1, 2), 5))

    def test_list_with_nested_structures(self): self.assertEqual(add_lists([[4, 5], {'a': 1}], (1, 2)), (1, 2, [4, 5], {'a': 1}))

    def test_large_input(self): self.assertEqual(add_lists(list(range(1000)), (0,)), tuple([0] + list(range(1000))))

    def test_original_tuple_unchanged(self):
        t = (1, 2)
        add_lists([3], t)
        self.assertEqual(t, (1, 2))

