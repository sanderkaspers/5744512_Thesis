import unittest
from datasets.GPT_4.Few_shot.programs.program_091 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_even_pair([2, 4, 6, 8]), 6) # All even numbers)

    def test_case_2(self):
        self.assertEqual(find_even_pair([1, 3, 5, 7]), 0) # No even numbers)

    def test_case_3(self):
        self.assertEqual(find_even_pair([2, 3, 4, 5]), 1) # Mixed even and odd numbers)

    def test_case_4(self):
        self.assertEqual(find_even_pair([]), 0) # Empty list)

    def test_case_5(self):
        self.assertEqual(find_even_pair([2]), 0) # Single even number)

    def test_case_6(self):
        self.assertEqual(find_even_pair([2, 4, 6]), 3) # Smaller list with even numbers)

    def test_case_7(self):
        self.assertEqual(find_even_pair([10, 20, 30, 40, 50]), 10) # Larger even numbers)

    def test_case_8(self):
        self.assertEqual(find_even_pair([2, 2, 2, 2]), 6) # List with repeated even numbers)

