import unittest
from datasets.mbpp.programs.program_025 import *

class TestVersion(unittest.TestCase):
    def test_is_samepatterns_with__red___green___green___a___b___b__expect_True(self):
        self.assertEqual(is_samepatterns(["red", "green", "green"], ["a", "b", "b"]), True)

    def test_is_samepatterns_with__red___green___greenn___a___b___b__expect_False(self):
        self.assertEqual(is_samepatterns(["red", "green", "greenn"], ["a", "b", "b"]), False)

    def test_is_samepatterns_with__red___green___greenn___a___b__expect_False(self):
        self.assertEqual(is_samepatterns(["red", "green", "greenn"], ["a", "b"]), False)

