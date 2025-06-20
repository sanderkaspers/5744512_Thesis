import unittest
from datasets.GPT_4.Few_shot1.programs.program_043 import *

class TestVersion(unittest.TestCase):
    def test_min_length_basic(self): self.assertEqual(Find_Min_Length(["hi", "hello", "hey"]), 2)

    def test_min_length_same_lengths(self): self.assertEqual(Find_Min_Length(["one", "two", "six"]), 3)

    def test_min_length_single_element(self): self.assertEqual(Find_Min_Length(["justone"]), 7)

    def test_min_length_includes_empty(self): self.assertEqual(Find_Min_Length(["full", "", "words"]), 0)

    def test_min_length_all_empty(self): self.assertEqual(Find_Min_Length(["", "", ""]), 0)

