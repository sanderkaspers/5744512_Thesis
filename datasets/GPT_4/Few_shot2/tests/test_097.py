import unittest
from datasets.GPT_4.Few_shot2.programs.program_097 import *

class TestVersion(unittest.TestCase):
    def test_check_type_all_tuples(self): self.assertTrue(check_type(((1,), (2, 3), (4, 5))))

    def test_check_type_with_list(self): self.assertFalse(check_type(((1,), [2, 3], (4, 5))))

    def test_check_type_with_string(self): self.assertFalse(check_type(((1,), 'not a tuple', (4,))))

    def test_check_type_with_dict(self): self.assertFalse(check_type(((1,), {'a': 1}, (4,))))

    def test_check_type_empty_outer_tuple(self): self.assertTrue(check_type(()))

    def test_check_type_all_empty_inner_tuples(self): self.assertTrue(check_type(((), (), ())))

    def test_check_type_single_non_tuple(self): self.assertFalse(check_type(('abc',)))

    def test_check_type_mixed_types(self): self.assertFalse(check_type(((1,), 2, 'x', (3,))))

    def test_check_type_nested_tuple(self): self.assertTrue(check_type((((1,),), ((2,),), ((3,),))))

