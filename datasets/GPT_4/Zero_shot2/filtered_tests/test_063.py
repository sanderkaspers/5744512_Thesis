import unittest
from datasets.GPT_4.Zero_shot2.programs.program_063 import *

class TestVersion(unittest.TestCase):
    def test_search_1(self):
        self.assertEqual(search([1, 2, 2]), 1)

    def test_search_2(self):
        self.assertEqual(search([4, 1, 2, 1, 2]), 4)

    def test_search_3(self):
        self.assertEqual(search([5, 3, 3]), 5)

    def test_search_4(self):
        self.assertEqual(search([3, 3, 6]), 6)

    def test_search_5(self):
        self.assertEqual(search([7, 9, 7]), 9)

    def test_search_6(self):
        self.assertEqual(search([10]), 10)

    def test_search_7(self):
        self.assertEqual(search([-1, -1, -2]), -2)

    def test_search_8(self):
        self.assertEqual(search([]), 0)

    def test_search_9(self):
        self.assertEqual(search([2, 2, 2, 2]), 0)

