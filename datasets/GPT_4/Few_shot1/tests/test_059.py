import unittest
from datasets.GPT_4.Few_shot1.programs.program_059 import *

class TestVersion(unittest.TestCase):
    def test_empty_dit_all_empty(self): self.assertEqual(empty_dit([{}, {}, {}]), True)

    def test_empty_dit_mixed(self): self.assertEqual(empty_dit([{}, {'a': 1}, {}]), False)

    def test_empty_dit_all_non_empty(self): self.assertEqual(empty_dit([{'a': 1}, {'b': 2}]), False)

    def test_empty_dit_single_empty(self): self.assertEqual(empty_dit([{}]), True)

    def test_empty_dit_single_non_empty(self): self.assertEqual(empty_dit([{'key': 'value'}]), False)

    def test_empty_dit_empty_list(self): self.assertEqual(empty_dit([]), True)

    def test_empty_dit_nested_dict(self): self.assertEqual(empty_dit([{}, {'nested': {}}]), False)

