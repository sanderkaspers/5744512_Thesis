import unittest
from datasets.GPT_4.Zero_shot1.programs.program_063 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(search([1, 2, 2, 1, 3]), 3)

    def test_2(self):
        self.assertEqual(search([7]), 7)

    def test_3(self):
        self.assertEqual(search([4, 5, 5, 6, 4, 7, 6]), 7)

    def test_4(self):
        self.assertEqual(search([9, 2, 2, 3, 3]), 9)

    def test_5(self):
        self.assertEqual(search([1, 1, 2]), 2)

    def test_6(self):
        self.assertEqual(search([-1, -1, 0]), 0)

    def test_7(self):
        self.assertEqual(search([1, 1, 2, 2]), 0)

    def test_8(self):
        self.assertEqual(search([]), 0)

    def test_9(self):
        self.assertEqual(search([True, False, True]), 1)

    def test_10(self):
        self.assertIsInstance(search([2, 2, 3]), int)

