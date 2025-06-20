import unittest
from datasets.GPT_4.Zero_shot2.programs.program_035 import *

class TestVersion(unittest.TestCase):
    def test_merge_1(self):
        self.assertEqual(merge_dictionaries_three({'a': 1}, {'b': 2}, {'c': 3}), {'a': 1, 'b': 2, 'c': 3})

    def test_merge_2(self):
        self.assertEqual(merge_dictionaries_three({'a': 1}, {'a': 2}, {'a': 3}), {'a': 1})

    def test_merge_3(self):
        self.assertEqual(merge_dictionaries_three({}, {'a': 2}, {'a': 3}), {'a': 2})

    def test_merge_4(self):
        self.assertEqual(merge_dictionaries_three({}, {}, {'a': 3}), {'a': 3})

    def test_merge_5(self):
        self.assertEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_merge_6(self):
        self.assertEqual(merge_dictionaries_three({'x': 10}, {}, {}), {'x': 10})

    def test_merge_7(self):
        self.assertEqual(merge_dictionaries_three({'x': 1}, {'x': 2}, {'x': 3}), {'x': 1})

    def test_merge_8(self):
        self.assertEqual(merge_dictionaries_three({'a': {'x': 1}}, {'b': {'y': 2}}, {'c': {'z': 3}}),
        {'a': {'x': 1}, 'b': {'y': 2}, 'c': {'z': 3}})

    def test_merge_9(self):
        self.assertEqual(merge_dictionaries_three({'a': None}, {'b': None}, {'c': None}),
        {'a': None, 'b': None, 'c': None})

    def test_merge_10(self):
        d1 = {str(i): i for i in range(100)}
        d2 = {str(i): i+100 for i in range(100, 200)}
        d3 = {str(i): i+200 for i in range(200, 300)}
        self.assertEqual(merge_dictionaries_three(d1, d2, d3), {**d3, **d2, **d1})

