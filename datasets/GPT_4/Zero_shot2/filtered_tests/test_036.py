import unittest
from datasets.GPT_4.Zero_shot2.programs.program_036 import *

class TestVersion(unittest.TestCase):
    def test_freq_1(self):
        self.assertEqual(freq_count([1, 2, 3]), {1: 1, 2: 1, 3: 1})

    def test_freq_2(self):
        self.assertEqual(freq_count([1, 1, 2, 2, 2]), {1: 2, 2: 3})

    def test_freq_3(self):
        self.assertEqual(freq_count([7, 7, 7, 7]), {7: 4})

    def test_freq_4(self):
        self.assertEqual(freq_count([]), {})

    def test_freq_5(self):
        self.assertEqual(freq_count(["a", 1, "a", 2]), {"a": 2, 1: 1, 2: 1})

    def test_freq_6(self):
        self.assertEqual(freq_count([-1, -1, 0, 1]), {-1: 2, 0: 1, 1: 1})

    def test_freq_7(self):
        self.assertEqual(freq_count([i % 5 for i in range(100)]),
        {0: 20, 1: 20, 2: 20, 3: 20, 4: 20})

    def test_freq_8(self):
        self.assertEqual(freq_count([1.1, 2.2, 1.1]), {1.1: 2, 2.2: 1})

    def test_freq_9(self):
        self.assertEqual(freq_count([True, False, True]), {True: 2, False: 1})

    def test_freq_10(self):
        self.assertEqual(freq_count([(1, 2), (1, 2), (3, 4)]),
        {(1, 2): 2, (3, 4): 1})

