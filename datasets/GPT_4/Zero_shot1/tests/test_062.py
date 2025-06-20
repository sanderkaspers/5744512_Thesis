import unittest
from datasets.GPT_4.Zero_shot1.programs.program_062 import *

class TestVersion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(string_to_list("abc"), ['a', 'b', 'c'])

    def test_2(self):
        self.assertEqual(string_to_list(""), [])

    def test_3(self):
        self.assertEqual(string_to_list("x"), ['x'])

    def test_4(self):
        self.assertEqual(string_to_list("a b"), ['a', ' ', 'b'])

    def test_5(self):
        self.assertEqual(string_to_list("!@#"), ['!', '@', '#'])

    def test_6(self):
        self.assertEqual(string_to_list("123"), ['1', '2', '3'])

    def test_7(self):
        self.assertEqual(string_to_list("a1!"), ['a', '1', '!'])

    def test_8(self):
        self.assertEqual(string_to_list("🔥"), ['🔥'])

    def test_9(self):
        self.assertIsInstance(string_to_list("ok"), list)

