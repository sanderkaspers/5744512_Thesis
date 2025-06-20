import unittest
from datasets.GPT_4.Few_shot.programs.program_072 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_occurrences(["apple", "banana", "apple", "orange", "banana", "apple"]), "apple") # Maximum occurring word)

    def test_case_2(self):
        self.assertEqual(max_occurrences(["apple", "banana", "orange"]), "apple") # All unique, return first in the tie)

    def test_case_3(self):
        self.assertEqual(max_occurrences(["a", "b", "c", "a", "b", "c", "a"]), "a") # Clear maximum)

    def test_case_4(self):
        self.assertEqual(max_occurrences([]), "") # Empty list)

    def test_case_5(self):
        self.assertEqual(max_occurrences(["apple!"]), "apple!") # Single word with special character)

    def test_case_6(self):
        self.assertEqual(max_occurrences(["apple", "apple", "apple"]), "apple") # All same word)

    def test_case_7(self):
        self.assertEqual(max_occurrences(["A", "B", "A", "B", "C", "B"]), "B") # Mixed case with clear maximum)

    def test_case_8(self):
        self.assertEqual(max_occurrences(["apple", "banana", "banana", "banana", "apple", "banana"]), "banana") # Repeated maximum)

