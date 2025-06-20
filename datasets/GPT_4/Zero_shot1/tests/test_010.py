import unittest
from datasets.GPT_4.Zero_shot1.programs.program_010 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_Max_Num([5, 4, 3, 2, 1]), 5)

    def test_2(self):
        self.assertEqual(find_Max_Num([0, -1, -2, -3]), 0)

    def test_3(self):
        self.assertEqual(find_Max_Num([100]), 100)

    def test_4(self):
        self.assertEqual(find_Max_Num([-5, -10, -3, -1]), -1)

    def test_5(self):
        self.assertEqual(find_Max_Num([3, 3, 3]), 3)

    def test_6(self):
        self.assertEqual(find_Max_Num([10, 20, 20, 10]), 20)

    def test_7(self):
        self.assertEqual(find_Max_Num([1.1, 2.2, 3.3, 2.2]), 3.3)

    def test_8(self):
        self.assertEqual(find_Max_Num([999, 1000, 998]), 1000)

    def test_9(self):
        self.assertEqual(find_Max_Num([-100, -200, -150]), -100)

