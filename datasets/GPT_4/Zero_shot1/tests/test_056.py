import unittest
from datasets.GPT_4.Zero_shot1.programs.program_056 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(odd_Equivalent("101", 6), 2)

    def test_2(self):
        self.assertEqual(odd_Equivalent("101", 7), 2)

    def test_3(self):
        self.assertEqual(odd_Equivalent("000", 9), 0)

    def test_4(self):
        self.assertEqual(odd_Equivalent("101010", 6), 0)

    def test_5(self):
        self.assertEqual(odd_Equivalent("010101", 6), 3)

    def test_6(self):
        self.assertEqual(odd_Equivalent("0", 5), 0)

    def test_7(self):
        self.assertEqual(odd_Equivalent("1", 5), 0)

    def test_8(self):
        self.assertEqual(odd_Equivalent("101", 0), 0)

    def test_9(self):
        self.assertEqual(odd_Equivalent("10", 1000), 250)

