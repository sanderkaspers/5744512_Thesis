import unittest
from datasets.o3.programs.program_025 import *

class TestVersion(unittest.TestCase):
    def test_matching_simple(self):
        colors = ['red','blue','blue','red']
        patterns = ['a','b','b','a']
        self.assertTrue(is_samepatterns(colors, patterns))

    def test_mismatch_length(self):
        colors = ['red','blue']
        patterns = ['a','b','b']
        self.assertFalse(is_samepatterns(colors, patterns))

    def test_inconsistent_mapping(self):
        colors = ['red','blue','green']
        patterns = ['a','b','a']
        self.assertFalse(is_samepatterns(colors, patterns))

    def test_two_patterns_same_color(self):
        colors = ['red','red']
        patterns = ['a','b']
        self.assertFalse(is_samepatterns(colors, patterns))

    def test_unique_one_to_one(self):
        colors = ['red','blue','green']
        patterns = ['a','b','c']
        self.assertTrue(is_samepatterns(colors, patterns))

    def test_large_unique_patterns(self):
        colors = ['color'+str(i) for i in range(50)]
        patterns = ['p'+str(i) for i in range(50)]
        self.assertTrue(is_samepatterns(colors, patterns))

