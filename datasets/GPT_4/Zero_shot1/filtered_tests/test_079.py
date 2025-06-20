import unittest
from datasets.GPT_4.Zero_shot1.programs.program_079 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(circle_circumference(0), 0.0)

    def test_2(self):
        self.assertAlmostEqual(circle_circumference(-2), -12.566)

    def test_3(self):
        self.assertAlmostEqual(circle_circumference(1e6), 6283000.0)

    def test_4(self):
        self.assertAlmostEqual(circle_circumference(0.5), 3.1415)

    def test_5(self):
        self.assertIsInstance(circle_circumference(1), float)

