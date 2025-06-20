import unittest
from datasets.GPT_4.Zero_shot1.programs.program_051 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(eulerian_num(0, 0), 0)

    def test_2(self):
        self.assertEqual(eulerian_num(5, 0), 1)

    def test_3(self):
        self.assertEqual(eulerian_num(5, 5), 0)

    def test_4(self):
        self.assertEqual(eulerian_num(4, 1), 11)

    def test_5(self):
        self.assertEqual(eulerian_num(5, 2), 66)

    def test_6(self):
        self.assertEqual(eulerian_num(1, 0), 1)

    def test_7(self):
        self.assertEqual(eulerian_num(2, 1), 1)

    def test_8(self):
        self.assertEqual(eulerian_num(3, 2), 1)

    def test_9(self):
        self.assertEqual(eulerian_num(15, 0), 1)

    def test_10(self):
        self.assertEqual(eulerian_num(6, 5), 1)

    def test_11(self):
        self.assertEqual(eulerian_num(4, 2), 11)

    def test_12(self):
        self.assertEqual(eulerian_num(True, False), 1)

    def test_13(self):
        self.assertIsInstance(eulerian_num(5, 2), int)

