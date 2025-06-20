import unittest
from datasets.GPT_4.Zero_shot1.programs.program_095 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(perimeter_pentagon(2.5), 12.5)

    def test_2(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_3(self):
        self.assertEqual(perimeter_pentagon(-3), -15)

    def test_4(self):
        self.assertEqual(perimeter_pentagon(1e6), 5e6)

    def test_5(self):
        self.assertAlmostEqual(perimeter_pentagon(0.1), 0.5, places=5)

    def test_6(self):
        self.assertIsInstance(perimeter_pentagon(1), (int, float))

