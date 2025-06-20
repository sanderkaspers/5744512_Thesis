import unittest
from datasets.GPT_4.Zero_shot1.programs.program_036 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(freq_count([1, 2, 3]), {1: 1, 2: 1, 3: 1})

    def test_2(self):
        self.assertEqual(freq_count([7, 7, 7]), {7: 3})

    def test_3(self):
        self.assertEqual(freq_count([]), {})

    def test_4(self):
        self.assertEqual(freq_count([-1, -1, 0]), {-1: 2, 0: 1})

    def test_5(self):
        self.assertEqual(freq_count([1.1, 2.2, 1.1]), {1.1: 2, 2.2: 1})

    def test_6(self):
        self.assertEqual(freq_count(["a", "b", "a"]), {"a": 2, "b": 1})

    def test_7(self):
        self.assertEqual(freq_count([1, "1", 1]), {1: 2, "1": 1})

    def test_8(self):
        self.assertEqual(freq_count([(1, 2), (1, 2), (2, 3)]), {(1, 2): 2, (2, 3): 1})

    def test_9(self):
        self.assertEqual(freq_count([True, False, True]), {True: 2, False: 1})

    def test_10(self):
        self.assertEqual(freq_count([0, 1, 0, 1, 1]), {0: 2, 1: 3})

    def test_11(self):
        self.assertEqual(freq_count([" ", " ", "a"]), {" ": 2, "a": 1})

    def test_12(self):
        self.assertEqual(freq_count(["A", "a"]), {"A": 1, "a": 1})

    def test_13(self):
        self.assertEqual(freq_count([None, None, 1]), {None: 2, 1: 1})

    def test_14(self):
        self.assertEqual(freq_count([i % 10 for i in range(100)]), {i: 10 for i in range(10)})

    def test_15(self):
         class Dummy: pass
                d = Dummy()
                self.assertEqual(freq_count([d, d]), {d: 2})

