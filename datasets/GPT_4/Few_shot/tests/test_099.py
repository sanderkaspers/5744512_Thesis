import unittest
from datasets.GPT_4.Few_shot.programs.program_099 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_Set_Bits(5), 2) # Binary 101)

    def test_case_2(self):
        self.assertEqual(count_Set_Bits(7), 3) # Binary 111)

    def test_case_3(self):
        self.assertEqual(count_Set_Bits(0), 0) # Binary 0)

    def test_case_4(self):
        self.assertEqual(count_Set_Bits(15), 4) # Binary 1111)

    def test_case_5(self):
        self.assertEqual(count_Set_Bits(1), 1) # Binary 1)

    def test_case_6(self):
        self.assertEqual(count_Set_Bits(8), 1) # Binary 1000)

    def test_case_7(self):
        self.assertEqual(count_Set_Bits(1023), 10) # Large number, binary 1111111111)

    def test_case_8(self):
        self.assertEqual(count_Set_Bits(255), 8) # Binary 11111111)

