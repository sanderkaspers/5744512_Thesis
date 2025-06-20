import unittest
from datasets.mbpp.programs.program_039 import *

class TestVersion(unittest.TestCase):
    def test_find_substring_with__red___black___white___green___orange___ack__expect_Tru(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"],"ack"), True)

    def test_find_substring_with__red___black___white___green___orange___abc__expect_Fal(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"],"abc"), False)

    def test_find_substring_with__red___black___white___green___orange___ange__expect_Tr(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"],"ange"), True)

