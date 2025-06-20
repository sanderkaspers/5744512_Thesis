import unittest
from datasets.GPT_4.Zero_shot2.programs.program_086 import *

class TestVersion(unittest.TestCase):
    def test_rem_1(self):
        self.assertEqual(remove_elements([1, 2, 3], [2]), [1, 3])

    def test_rem_2(self):
        self.assertEqual(remove_elements([1, 2, 3], [4, 5]), [1, 2, 3])

    def test_rem_3(self):
        self.assertEqual(remove_elements([1, 2, 3], [1, 2, 3]), [])

    def test_rem_4(self):
        self.assertEqual(remove_elements([], [1, 2]), [])

    def test_rem_5(self):
        self.assertEqual(remove_elements([1, 2], []), [1, 2])

    def test_rem_6(self):
        self.assertEqual(remove_elements([], []), [])

    def test_rem_7(self):
        self.assertEqual(remove_elements([1, 1, 2], [1]), [2])

    def test_rem_8(self):
        self.assertEqual(remove_elements(['a', 'A'], ['A']), ['a'])

    def test_rem_9(self):
        self.assertEqual(remove_elements([1, '1', 1.0], [1]), ['1'])

    def test_rem_10(self):
        self.assertEqual(remove_elements([[1, 2]], [[1, 2]]), [[1, 2]])

    def test_rem_11(self):
        self.assertEqual(remove_elements([1, 2, 3], [1, 2, 3]), [])

