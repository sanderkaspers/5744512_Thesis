import unittest
from datasets.GPT_4.Zero_shot1.programs.program_035 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(merge_dictionaries({'a': 1}, {'a': 2}), {'a': 3})

    def test_2(self):
        self.assertEqual(merge_dictionaries({}, {'a': 2}), {'a': 2})

    def test_3(self):
        self.assertEqual(merge_dictionaries({}, {}), {})

    def test_4(self):
        self.assertEqual(merge_dictionaries({'a': 0}, {'a': 0}), {'a': 0})

    def test_5(self):
        self.assertEqual(merge_dictionaries({'a': -1}, {'a': -2}), {'a': -3})

    def test_6(self):
        self.assertEqual(merge_dictionaries({'a': 1.5}, {'a': 2.5}), {'a': 4.0})

    def test_7(self):
        self.assertEqual(merge_dictionaries({'a': 1}, merge_dictionaries({'a': 2}, {'a': 3})), {'a': 6})

    def test_8(self):
        self.assertEqual(merge_dictionaries({'a': 1.1}, {'a': 2.2}), {'a': 3.3})

    def test_9(self):
        from collections import Counter
        self.assertEqual(merge_dictionaries({'a': 1}, Counter({'a': 2})), {'a': 3})

    def test_10(self):
        big_dict = {str(i): i for i in range(1000)}
        self.assertEqual(len(merge_dictionaries(big_dict, big_dict)), 1000)

    def test_11(self):
        self.assertEqual(merge_dictionaries({'a': 2}, {'a': 2}), {'a': 4})

    def test_12(self):
        self.assertEqual(merge_dictionaries({'x': 1}, {'y': 2}), {'x': 1, 'y': 2})

    def test_13(self):
        self.assertEqual(merge_dictionaries({'Key': 1}, {'key': 2}), {'Key': 1, 'key': 2})

