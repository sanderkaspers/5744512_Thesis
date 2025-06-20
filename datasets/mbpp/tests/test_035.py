import unittest
from datasets.mbpp.programs.program_035 import *

class TestVersion(unittest.TestCase):
    def test_merge_case_1(self):
        self.assertEqual(
        merge_dictionaries_three(
        {"R": "Red", "B": "Black", "P": "Pink"},
        {"G": "Green", "W": "White"},
        {"O": "Orange", "W": "White", "B": "Black"}
        ),
        {"R": "Red", "B": "Black", "P": "Pink", "G": "Green", "W": "White", "O": "Orange"}
        )

    def test_merge_case_2(self):
        self.assertEqual(
        merge_dictionaries_three(
        {"R": "Red", "B": "Black", "P": "Pink"},
        {"G": "Green", "W": "White"},
        {"L": "lavender", "B": "Blue"}
        ),
        {"R": "Red", "B": "Black", "P": "Pink", "G": "Green", "W": "White", "L": "lavender"}
        )

    def test_merge_case_3(self):
        self.assertEqual(
        merge_dictionaries_three(
        {"R": "Red", "B": "Black", "P": "Pink"},
        {"L": "lavender", "B": "Blue"},
        {"G": "Green", "W": "White"}
        ),
        {"R": "Red", "B": "Black", "P": "Pink", "L": "lavender", "G": "Green", "W": "White"}
        )

