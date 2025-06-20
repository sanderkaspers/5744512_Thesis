import unittest
from datasets.o3.programs.program_099 import *

class TestVersion(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_Set_Bits(0), 0)

    def test_one(self):
        self.assertEqual(count_Set_Bits(1), 1)

    def test_five(self):
        self.assertEqual(count_Set_Bits(5), 2)

    def test_max_byte(self):
        self.assertEqual(count_Set_Bits(255), 8)

    def test_large_number(self):
        self.assertEqual(count_Set_Bits(4294967295), 32)

