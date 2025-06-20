import unittest
from datasets.GPT_4.Zero_shot1.programs.program_076 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(hexagonal_num(2), 6)

    def test_2(self):
        self.assertEqual(hexagonal_num(5), 45)

    def test_3(self):
        self.assertEqual(hexagonal_num(0), 0)

    def test_4(self):
        self.assertEqual(hexagonal_num(-3), -15)

    def test_5(self):
        self.assertIsInstance(hexagonal_num(3), int)

