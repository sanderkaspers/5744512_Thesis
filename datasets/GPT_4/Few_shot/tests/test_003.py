import unittest
from datasets.GPT_4.Few_shot.programs.program_003 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_Volume(0, 0, 0), 0)

    def test_case_2(self):
        self.assertEqual(find_Volume(1, 2, 3), 3.0)

    def test_case_3(self):
        self.assertEqual(find_Volume(10, 10, 10), 500.0)

    def test_case_4(self):
        self.assertEqual(find_Volume(5, 5, 0), 0)

    def test_case_5(self):
        self.assertEqual(find_Volume(1000000, 1000000, 1000000), 500000000000000.0)

    def test_case_6(self):
        self.assertEqual(find_Volume(2, 2, 2), 4.0)

    def test_case_7(self):
        self.assertEqual(find_Volume(1, 2, 3), 3.0)

