import unittest
from datasets.GPT_4.Zero_shot2.programs.program_056 import *

class TestVersion(unittest.TestCase):
    def test_odd_1(self):
        self.assertEqual(odd_Equivalent("12345", 2), 6)

    def test_odd_2(self):
        self.assertEqual(odd_Equivalent("13579", 3), 15)

    def test_odd_3(self):
        self.assertEqual(odd_Equivalent("2468", 5), 0)

    def test_odd_4(self):
        self.assertEqual(odd_Equivalent("", 4), 0)

    def test_odd_5(self):
        self.assertEqual(odd_Equivalent("13579", 0), 0)

    def test_odd_6(self):
        self.assertEqual(odd_Equivalent("13579", 1), 5)

    def test_odd_7(self):
        self.assertEqual(odd_Equivalent("3", 4), 4)

    def test_odd_8(self):
        self.assertEqual(odd_Equivalent("135", 1000), 3000)

