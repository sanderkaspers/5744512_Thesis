import unittest
from datasets.GPT_4.Few_shot2.programs.program_022 import *

class TestVersion(unittest.TestCase):
    def test_find_equal_tuple_basic(self): self.assertEqual(find_equal_tuple([(1, 2), (3, 4), (5,)]), [(1, 2), (3, 4)])

    def test_find_equal_tuple_all_equal(self): self.assertEqual(find_equal_tuple([(1, 2), (3, 4)]), [(1, 2), (3, 4)])

    def test_find_equal_tuple_none_equal(self): self.assertEqual(find_equal_tuple([(1, 2), (3,), (4, 5, 6)]), [(1, 2)])

    def test_find_equal_tuple_first_longest(self): self.assertEqual(find_equal_tuple([(1, 2, 3), (4, 5), (6,)]), [(1, 2, 3)])

    def test_find_equal_tuple_first_shortest(self): self.assertEqual(find_equal_tuple([(1,), (2, 3), (4, 5, 6)]), [(1,)])

    def test_find_equal_tuple_empty_input(self): self.assertEqual(find_equal_tuple([]), [])

    def test_find_equal_tuple_single_tuple(self): self.assertEqual(find_equal_tuple([(1, 2)]), [(1, 2)])

    def test_find_equal_tuple_with_empty_tuple_first(self): self.assertEqual(find_equal_tuple([(), (1,), (2, 3)]), [()])

    def test_find_equal_tuple_all_empty_tuples(self): self.assertEqual(find_equal_tuple([(), (), ()]), [(), (), ()])

