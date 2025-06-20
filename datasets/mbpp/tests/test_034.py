import unittest
from datasets.mbpp.programs.program_034 import *

class TestVersion(unittest.TestCase):
    def test_centered_hexagonal_number_with_10_expect_271(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

    def test_centered_hexagonal_number_with_2_expect_7(self):
        self.assertEqual(centered_hexagonal_number(2), 7)

    def test_centered_hexagonal_number_with_9_expect_217(self):
        self.assertEqual(centered_hexagonal_number(9), 217)

