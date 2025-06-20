import unittest
from datasets.GPT_4.Zero_shot1.programs.program_005 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_2(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_3(self):
        self.assertEqual(square_perimeter(10), 40)

    def test_4(self):
        self.assertEqual(square_perimeter(2.5), 10.0)

    def test_5(self):
        self.assertEqual(square_perimeter(100), 400)

    def test_6(self):
        self.assertEqual(square_perimeter(0.1), 0.4)

    def test_7(self):
        self.assertEqual(square_perimeter(-3), -12)

    def test_8(self):
        self.assertEqual(square_perimeter(1e3), 4000.0)

    def test_9(self):
        self.assertEqual(square_perimeter(7.75), 31.0)

