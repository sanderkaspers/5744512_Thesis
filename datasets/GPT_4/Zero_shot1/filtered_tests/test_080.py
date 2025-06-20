import unittest
from datasets.GPT_4.Zero_shot1.programs.program_080 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(extract_singly([[5, 6], [7, 8]]), [5, 6, 7, 8])

    def test_2(self):
        self.assertEqual(extract_singly([[1, 1], [1], [1, 1]]), [1])

    def test_3(self):
        self.assertEqual(extract_singly([[1, 2], [], [2, 3]]), [1, 2, 3])

    def test_4(self):
        self.assertEqual(extract_singly([]), [])

    def test_5(self):
        self.assertEqual(extract_singly([[], [], []]), [])

    def test_6(self):
        self.assertEqual(extract_singly([[1, "1", 2]]), [1, "1", 2])

    def test_7(self):
        self.assertEqual(extract_singly([[1], ["1"], [1, "1"]]), [1, "1"])

    def test_8(self):
        self.assertEqual(extract_singly([[0]*1000]), [0])

    def test_9(self):
        self.assertIsInstance(extract_singly([[1, 2], [3]]), list)

