import unittest
from datasets.mbpp.programs.program_051 import *

class TestVersion(unittest.TestCase):
    def test_eulerian_num_with_3_1_expect_4(self):
        self.assertEqual(eulerian_num(3, 1), 4)

    def test_eulerian_num_with_4_1_expect_11(self):
        self.assertEqual(eulerian_num(4, 1), 11)

    def test_eulerian_num_with_5_3_expect_26(self):
        self.assertEqual(eulerian_num(5, 3), 26)

