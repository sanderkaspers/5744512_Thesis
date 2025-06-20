import unittest
from datasets.GPT_4.Few_shot1.programs.program_038 import *

class TestVersion(unittest.TestCase):
    def test_len_log_basic(self): self.assertEqual(len_log(["hi", "hello", "hey"]), "hello")

    def test_len_log_single_element(self): self.assertEqual(len_log(["alone"]), "alone")

    def test_len_log_multiple_max(self): self.assertEqual(len_log(["a", "bb", "cc"]), "bb")

    def test_len_log_empty_string_in_list(self): self.assertEqual(len_log(["", "abc", "de"]), "abc")

    def test_len_log_long_first(self): self.assertEqual(len_log(["longword", "short", "tiny"]), "longword")

    def test_len_log_all_empty(self): self.assertEqual(len_log(["", "", ""]), "")

