import unittest
from datasets.GPT_4.Zero_shot1.programs.program_025 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_samepatterns(['red', 'green', 'red'], ['a', 'b', 'c']), False)

    def test_2(self):
        self.assertEqual(is_samepatterns(['x', 'y', 'z'], ['a', 'b', 'c']), True)

    def test_3(self):
        self.assertEqual(is_samepatterns(['x', 'x', 'y'], ['a', 'b', 'a']), False)

    def test_4(self):
        self.assertEqual(is_samepatterns(['a'], ['b']), True)

    def test_5(self):
        self.assertEqual(is_samepatterns([], []), True)

    def test_6(self):
        self.assertEqual(is_samepatterns(['a', 'b'], ['x']), False)

    def test_7(self):
        self.assertEqual(is_samepatterns(['a', 'a'], ['x', 'x']), True)

    def test_8(self):
        self.assertEqual(is_samepatterns(['a', 'b'], ['x', 'x']), False)

