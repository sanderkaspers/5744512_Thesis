import unittest
from datasets.GPT_4.Few_shot1.programs.program_097 import *

class TestVersion(unittest.TestCase):
    def test_check_type_all_int(self): self.assertTrue(check_type((1, 2, 3)))

    def test_check_type_all_str(self): self.assertTrue(check_type(("a", "b", "c")))

    def test_check_type_all_float(self): self.assertTrue(check_type((1.0, 2.5, 3.14)))

    def test_check_type_all_bool(self): self.assertTrue(check_type((True, False, True)))

    def test_check_type_all_same_object(self):
        obj = object()
        self.assertTrue(check_type((obj, obj, obj)))

    def test_check_type_diff_first(self): self.assertFalse(check_type((1, "1", 2)))

    def test_check_type_diff_middle(self): self.assertFalse(check_type(("a", 1, "b")))

    def test_check_type_diff_end(self): self.assertFalse(check_type((1.1, 2.2, "3.3")))

    def test_check_type_empty(self): self.assertTrue(check_type(()))

    def test_check_type_single_element(self): self.assertTrue(check_type((42,)))

    def test_check_type_nested_tuple_same(self): self.assertTrue(check_type(((1, 2), (3, 4))))

    def test_check_type_nested_tuple_diff(self): self.assertFalse(check_type(((1, 2), [3, 4])))

    def test_check_type_mixed_bools_ints(self): self.assertTrue(check_type((True, False, 1)))

    def test_check_type_types_different(self): self.assertFalse(check_type((int, str)))

    def test_check_type_mixed_none_and_int(self): self.assertFalse(check_type((None, 1)))

