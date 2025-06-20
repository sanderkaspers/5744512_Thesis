import unittest
from datasets.mbpp.programs.program_022 import *

class TestVersion(unittest.TestCase):
    def test_case(self):
        self.assertEqual(get_equal([(11, 22, 33), (44, 55, 66)]), True)

    def test_case2(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5, 6, 7)]), False)

    def test_case3(self):
        self.assertEqual(get_equal([(1, 2), (3, 4)]), True)

