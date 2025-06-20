import unittest
from datasets.o3.programs.program_036 import *

class TestVersion(unittest.TestCase):
    def test_basic_integers(self):
        import collections
        self.assertEqual(freq_count([1,1,2,2,2,3]), collections.Counter({2:3,1:2,3:1}))

    def test_strings(self):
        import collections
        self.assertEqual(freq_count(['a','b','a']), collections.Counter({'a':2,'b':1}))

    def test_empty_list(self):
        import collections
        self.assertEqual(freq_count([]), collections.Counter())

    def test_mixed_types(self):
        import collections
        self.assertEqual(freq_count([1,'1',1]), collections.Counter({1:2,'1':1}))

    def test_negative_numbers(self):
        import collections
        self.assertEqual(freq_count([-1,-1,0]), collections.Counter({-1:2,0:1}))

