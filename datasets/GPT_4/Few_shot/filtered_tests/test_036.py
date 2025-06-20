import unittest
from datasets.GPT_4.Few_shot.programs.program_036 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(freq_count([1, 2, 3, 4, 5]), {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}) # All unique elements)

    def test_case_2(self):
        self.assertEqual(freq_count([1, 1, 2, 2, 3, 3]), {1: 2, 2: 2, 3: 2}) # Repeated elements)

    def test_case_3(self):
        self.assertEqual(freq_count([]), {}) # Empty list)

    def test_case_4(self):
        self.assertEqual(freq_count([1, "a", 1, "a", 2, "b"]), {1: 2, "a": 2, 2: 1, "b": 1}) # Mixed data types)

    def test_case_5(self):
        self.assertEqual(freq_count([None, None, True, False, True]), {None: 2, True: 2, False: 1}) # None and boolean values)

    def test_case_6(self):
        self.assertEqual(freq_count(["apple", "apple", "banana", "apple", "banana", "cherry"]), {"apple": 3, "banana": 2, "cherry": 1}) # Strings)

    def test_case_7(self):
        self.assertEqual(freq_count([0, 0, 1, 1, 2, 2, 3, 3]), {0: 2, 1: 2, 2: 2, 3: 2}) # Numeric with repeats)

    def test_case_8(self):
        self.assertEqual(freq_count(["a", 1, "a", 1, 2, "b", "b", 1]), {"a": 2, 1: 3, 2: 1, "b": 2}) # Mixed data with repeats)

