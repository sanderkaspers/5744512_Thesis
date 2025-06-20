import unittest
from datasets.GPT_4.Zero_shot1.programs.program_085 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertIsNone(find_solution(4, 6, 7))

    def test_2(self):
        self.assertEqual(find_solution(5, 2, 10), (0, 5))

    def test_3(self):
        self.assertEqual(find_solution(2, 5, 10), (0, 2))

    def test_4(self):
        self.assertEqual(find_solution(3, 3, 6), (0, 2))

    def test_5(self):
        self.assertEqual(find_solution(11, 3, 9), (0, 3))

    def test_6(self):
        self.assertEqual(find_solution(1, 1, 0), (0, 0))

    def test_7(self):
        self.assertEqual(find_solution(7, 11, 1001), (6, 77))

    def test_8(self):
        self.assertIsNone(find_solution(-3, 5, 11))

    def test_9(self):
        self.assertIsNone(find_solution(3, 5, -11))

    def test_10(self):
        result = find_solution(4, 7, 23)
        self.assertTrue(result is None or isinstance(result, tuple))

    def test_11(self):
        self.assertIsNone(find_solution(7, 11, 1))

    def test_12(self):
        self.assertEqual(find_solution(0, 5, 10), (0, 2))

