import unittest
from datasets.mbpp.programs.program_079 import *

class TestVersion(unittest.TestCase):
    def test_circle_circumference_with_10_expect_62_830000000000005(self):
        self.assertEqual(circle_circumference(10), 62.830000000000005)

    def test_circle_circumference_with_5_expect_31_415000000000003(self):
        self.assertEqual(circle_circumference(5), 31.415000000000003)

    def test_circle_circumference_with_4_expect_25_132(self):
        self.assertEqual(circle_circumference(4), 25.132)

