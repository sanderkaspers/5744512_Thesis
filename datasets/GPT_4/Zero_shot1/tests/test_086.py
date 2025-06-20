import unittest
from datasets.GPT_4.Zero_shot1.programs.program_086 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(remove_elements([1, 2, 3], [2, 3]), [1])

    def test_2(self):
        self.assertEqual(remove_elements([1, 2], [1, 2, 3]), [])

    def test_3(self):
        self.assertEqual(remove_elements([1, 2], []), [1, 2])

    def test_4(self):
        self.assertEqual(remove_elements([], [1, 2]), [])

    def test_5(self):
        self.assertEqual(remove_elements([], []), [])

    def test_6(self):
        self.assertEqual(remove_elements([1, 1, 2], [1]), [2])

    def test_7(self):
        self.assertEqual(remove_elements([1, 2, 3], [2, 2]), [1, 3])

    def test_8(self):
        self.assertEqual(remove_elements([1, '1', True], [True]), [1, '1'])

    def test_9(self):
        self.assertEqual(remove_elements([[1, 2]], [[1, 2]]), [])

    def test_10(self):
        self.assertIsInstance(remove_elements([1, 2], [2]), list)

    def test_11(self):
        self.assertEqual(remove_elements([3, 2, 1], [2]), [3, 1])

