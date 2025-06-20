import unittest
from datasets.GPT_4.Zero_shot2.programs.program_010 import *

class TestVersion(unittest.TestCase):
    def test_max_1(self):
        self.assertEqual(find_Max_Num([1, 2, 3, 4, 5]), 5)

    def test_max_2(self):
        self.assertEqual(find_Max_Num([-1, -2, 0, 2, -3]), 2)

    def test_max_3(self):
        self.assertEqual(find_Max_Num([7, 7, 7, 7]), 7)

    def test_max_4(self):
        self.assertEqual(find_Max_Num([10]), 10)

    def test_max_5(self):
        self.assertEqual(find_Max_Num([-10, -20, -5, -15]), -5)

    def test_max_6(self):
        self.assertEqual(find_Max_Num([99, 1, 2, 3]), 99)

