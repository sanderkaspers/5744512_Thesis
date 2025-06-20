import unittest
from datasets.GPT_4.Zero_shot1.programs.program_049 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 3), 7)

    def test_2(self):
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 6), 20)

    def test_3(self):
        self.assertEqual(kth_element([1, 2, 2, 3], 2), 2)

    def test_4(self):
        self.assertEqual(kth_element([-1, -10, 5, 0], 2), -1)

    def test_5(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 3), 3)

    def test_6(self):
        self.assertEqual(kth_element([5, 4, 3, 2, 1], 3), 3)

    def test_7(self):
        self.assertEqual(kth_element([42], 1), 42)

    def test_8(self):
        self.assertEqual(kth_element([9, 7, 5, 3, 1], 5), 9)

    def test_9(self):
        self.assertEqual(kth_element([2, 2, 2], 2), 2)

    def test_10(self):
        self.assertEqual(kth_element([1.1, 2.2, 0.5], 2), 1.1)

    def test_11(self):
        self.assertEqual(kth_element([1, 2.2, 3.3], 2), 2.2)

    def test_12(self):
        self.assertEqual(kth_element([8, 3, 5], 2), 5)

    def test_13(self):
        arr = [9, 2, 5]
        kth_element(arr, 2)
        self.assertNotEqual(arr, [9, 2, 5])

    def test_14(self):
        self.assertEqual(kth_element([9, 1, 8, 2, 7, 3], 4), 7)

