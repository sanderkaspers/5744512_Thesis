import unittest
from datasets.GPT_4.Zero_shot2.programs.program_095 import *

class TestVersion(unittest.TestCase):
    def test_pent_1(self):
        self.assertEqual(perimeter_pentagon(1), 5)

    def test_pent_2(self):
        self.assertEqual(perimeter_pentagon(2.5), 12.5)

    def test_pent_3(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_pent_4(self):
        self.assertEqual(perimeter_pentagon(-1), -5)

    def test_pent_5(self):
        self.assertAlmostEqual(perimeter_pentagon(0.001), 0.005)

    def test_pent_6(self):
        self.assertEqual(perimeter_pentagon(1e6), 5e6)

    def test_pent_7(self):
        self.assertEqual(perimeter_pentagon(5.0), 25.0)

