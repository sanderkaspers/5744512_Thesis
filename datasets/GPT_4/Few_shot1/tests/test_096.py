import unittest
from datasets.GPT_4.Few_shot1.programs.program_096 import *

class TestVersion(unittest.TestCase):
    def test_count_occurance_basic(self): self.assertEqual(count_occurance("std"), 1)

    def test_count_occurance_multiple(self): self.assertEqual(count_occurance("stdstd"), 2)

    def test_count_occurance_none(self): self.assertEqual(count_occurance("abc"), 0)

    def test_count_occurance_overlap(self): self.assertEqual(count_occurance("ststdtd"), 1)

    def test_count_occurance_single_char(self): self.assertEqual(count_occurance("s"), 0)

    def test_count_occurance_two_chars(self): self.assertEqual(count_occurance("st"), 0)

    def test_count_occurance_prefix(self): self.assertEqual(count_occurance("stdabc"), 1)

    def test_count_occurance_suffix(self): self.assertEqual(count_occurance("abcstd"), 1)

    def test_count_occurance_middle(self): self.assertEqual(count_occurance("abstdcd"), 1)

    def test_count_occurance_with_spaces(self): self.assertEqual(count_occurance("s t d std"), 1)

    def test_count_occurance_uppercase(self): self.assertEqual(count_occurance("STDstd"), 1)

    def test_count_occurance_case_sensitive(self): self.assertEqual(count_occurance("StD"), 0)

    def test_count_occurance_empty(self): self.assertEqual(count_occurance(""), 0)

    def test_count_occurance_long_string(self): self.assertEqual(count_occurance("xstd"*100), 100)

    def test_count_occurance_separated(self): self.assertEqual(count_occurance("sxtxdy"), 0)

