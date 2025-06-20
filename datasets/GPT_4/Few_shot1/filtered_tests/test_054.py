import unittest
from datasets.GPT_4.Few_shot1.programs.program_054 import *

class TestVersion(unittest.TestCase):
    def test_add_lists_basic(self): self.assertEqual(add_lists([4, 5], (1, 2, 3)), (1, 2, 3, 4, 5))

    def test_add_lists_empty_list(self): self.assertEqual(add_lists([], (1, 2)), (1, 2))

    def test_add_lists_empty_tuple(self): self.assertEqual(add_lists([3, 4], ()), (3, 4))

    def test_add_lists_both_empty(self): self.assertEqual(add_lists([], ()), ())

    def test_add_lists_mixed_types(self): self.assertEqual(add_lists(['a', True], (1,)), (1, 'a', True))

    def test_add_lists_nested_elements(self): self.assertEqual(add_lists([[1], (2,)], ((0,),)), ((0,), [1], (2,)))

