import unittest
from datasets.GPT_4.Zero_shot1.programs.program_048 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(next_smallest_palindrome(123), 131)

    def test_2(self):
        self.assertEqual(next_smallest_palindrome(121), 131)

    def test_3(self):
        self.assertEqual(next_smallest_palindrome(7), 8)

    def test_4(self):
        result = next_smallest_palindrome(999999)
        self.assertTrue(str(result) == str(result)[::-1])

    def test_5(self):
        self.assertEqual(next_smallest_palindrome(999), 1001)

    def test_6(self):
        self.assertEqual(next_smallest_palindrome(89), 99)

    def test_7(self):
        self.assertEqual(next_smallest_palindrome(10), 11)

    def test_8(self):
        self.assertEqual(next_smallest_palindrome(777), 787)

    def test_9(self):
        self.assertEqual(next_smallest_palindrome(130), 131)

    def test_10(self):
        self.assertEqual(next_smallest_palindrome(0), 1)

    def test_11(self):
        self.assertEqual(next_smallest_palindrome(1), 2)

    def test_12(self):
        self.assertEqual(next_smallest_palindrome(-10), 1)

    def test_13(self):
        self.assertEqual(next_smallest_palindrome(True), 2)

    def test_14(self):
        self.assertEqual(next_smallest_palindrome(9), 11)

    def test_15(self):
        result = next_smallest_palindrome(122221)
        self.assertTrue(str(result) == str(result)[::-1])

    def test_16(self):
        result = next_smallest_palindrome(12321)
        self.assertTrue(str(result) == str(result)[::-1])

    def test_17(self):
        val = next_smallest_palindrome(150)
        self.assertEqual(str(val), str(val)[::-1])

    def test_18(self):
        val = next_smallest_palindrome(101)
        self.assertGreater(val, 101)

