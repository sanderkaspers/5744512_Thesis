import unittest
from datasets.GPT_4.Zero_shot2.programs.program_080 import *

class TestVersion(unittest.TestCase):
    def test_single_1(self):
        self.assertEqual(extract_singly([1, 2, 2, 3, 4, 4]), [1, 3])

    def test_single_2(self):
        self.assertEqual(extract_singly([5, 6, 7]), [5, 6, 7])

    def test_single_3(self):
        self.assertEqual(extract_singly([2, 2, 2]), [])

    def test_single_4(self):
        self.assertEqual(extract_singly([]), [])

    def test_single_5(self):
        self.assertEqual(extract_singly([1]), [1])

    def test_single_6(self):
        self.assertEqual(extract_singly([-1, 2, -1, 3]), [2, 3])

    def test_single_7(self):
        self.assertEqual(extract_singly(['a', 'b', 'a', 'c']), ['b', 'c'])

    def test_single_8(self):
        self.assertEqual(extract_singly([1, '1', 1.0]), ['1'])

    def test_single_9(self):
        self.assertEqual(extract_singly(list(range(100)) + [50, 60]), [i for i in range(100) if i != 50 and i != 60])

    def test_single_10(self):
        self.assertEqual(extract_singly(['Apple', 'apple', 'Banana', 'banana', 'apple']), ['Apple', 'Banana', 'banana'])

