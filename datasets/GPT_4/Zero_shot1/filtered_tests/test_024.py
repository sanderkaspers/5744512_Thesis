import unittest
from datasets.GPT_4.Zero_shot1.programs.program_024 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(dif_Square(1), True)

    def test_2(self):
        self.assertEqual(dif_Square(2), False)

    def test_3(self):
        self.assertEqual(dif_Square(3), True)

    def test_4(self):
        self.assertEqual(dif_Square(4), True)

    def test_5(self):
        self.assertEqual(dif_Square(-2), False)

    def test_6(self):
        self.assertEqual(dif_Square(-5), True)

    def test_7(self):
        self.assertEqual(dif_Square(1000000), True)

