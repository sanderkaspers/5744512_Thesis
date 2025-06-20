import unittest
from datasets.GPT_4.Few_shot.programs.program_063 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(search([1, 2, 2, 1, 3]), 3) # Unique element is 3)

    def test_case_2(self):
        self.assertEqual(search([4, 4, 5, 5, 6]), 6) # Unique element is 6)

    def test_case_3(self):
        self.assertEqual(search([7]), 7) # Single element)

    def test_case_4(self):
        self.assertEqual(search([-1, 2, 2, -1, 3]), 3) # Unique element with negative numbers)

    def test_case_5(self):
        self.assertEqual(search([0, 1, 0, 1, -2]), -2) # Unique element is negative)

    def test_case_6(self):
        self.assertEqual(search([10, 20, 20, 10, 30]), 30) # Unique element is positive)

    def test_case_7(self):
        self.assertEqual(search([-3, -3, -4, -4, 5]), 5) # Mixed positive and negative)

    def test_case_8(self):
        self.assertEqual(search([1, 1, 2, 2, 3, 3, 4]), 4) # Unique element is last)

