import unittest
from datasets.GPT_4.Zero_shot2.programs.program_003 import *

class TestVersion(unittest.TestCase):
    def test_find_volume_1(self):
        self.assertEqual(find_Volume(2, 3, 4), 12.0)

    def test_find_volume_2(self):
        self.assertEqual(find_Volume(0, 5, 10), 0.0)

    def test_find_volume_3(self):
        self.assertAlmostEqual(find_Volume(1.5, 2.0, 3.0), 4.5)

    def test_find_volume_4(self):
        self.assertEqual(find_Volume(1000, 2000, 3000), 3000000000.0)

    def test_find_volume_5(self):
        self.assertEqual(find_Volume(-1, 2, 3), -3.0)

