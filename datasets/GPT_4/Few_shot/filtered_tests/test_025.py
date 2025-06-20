import unittest
from datasets.GPT_4.Few_shot.programs.program_025 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_samepatterns(["red", "blue", "blue"], ["a", "b", "b"]), True) # Same pattern)

    def test_case_2(self):
        self.assertEqual(is_samepatterns(["red", "blue", "blue"], ["a", "b", "c"]), False) # Different pattern)

    def test_case_3(self):
        self.assertEqual(is_samepatterns(["red", "blue"], ["a", "b", "b"]), False) # Different lengths)

    def test_case_4(self):
        self.assertEqual(is_samepatterns([], []), True) # Both lists empty)

    def test_case_5(self):
        self.assertEqual(is_samepatterns(["red", "blue"], ["a", "a"]), False) # Different pattern)

    def test_case_6(self):
        self.assertEqual(is_samepatterns(["red", "red", "red"], ["a", "a", "a"]), True) # Same pattern, repeated elements)

    def test_case_7(self):
        self.assertEqual(is_samepatterns(["red", "blue", "green"], ["a", "b", "c"]), True) # Different colors, different patterns)

    def test_case_8(self):
        self.assertEqual(is_samepatterns(["red", "blue", "blue"], ["a", "a", "b"]), False) # Mixed pattern)

