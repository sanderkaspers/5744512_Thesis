import unittest
from datasets.GPT_4.Zero_shot1.programs.program_099 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_Set_Bits(1), 1)

    def test_2(self):
        self.assertEqual(count_Set_Bits(2), 1)

    def test_3(self):
        self.assertEqual(count_Set_Bits(3), 2)

    def test_4(self):
        self.assertEqual(count_Set_Bits(15), 4)

    def test_5(self):
        self.assertEqual(count_Set_Bits(2**20), 1)

    def test_6(self):
        self.assertIsInstance(count_Set_Bits(31), int)

