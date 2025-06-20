import unittest
from datasets.o3.programs.program_063 import *

class TestVersion(unittest.TestCase):
    def test_basic_xor(self):
        self.assertEqual(search([1,2,3]), 1^2^3)

    def test_single_element(self):
        self.assertEqual(search([42]), 42)

    def test_empty_array(self):
        self.assertEqual(search([]), 0)

    def test_with_zero(self):
        self.assertEqual(search([0,0,5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(search([-1,-1,2]), 2)

