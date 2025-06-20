import unittest
from datasets.GPT_4.Zero_shot.programs.program_052 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        input_list = [["banana", "apple", "cherry"], ["dog", "cat", "elephant"]]
        expected_output = [["apple", "banana", "cherry"], ["cat", "dog", "elephant"]]
        assert sort_sublists(input_list) == expected_output

    def test_multiple_spaces_2(self):
        input_list = [["apple", "banana", "cherry"], ["cat", "dog", "elephant"]]
        expected_output = [["apple", "banana", "cherry"], ["cat", "dog", "elephant"]]
        assert sort_sublists(input_list) == expected_output

    def test_multiple_spaces_3(self):
        input_list = [["apple", "banana"], [], ["dog", "cat"]]
        expected_output = [["apple", "banana"], [], ["cat", "dog"]]
        assert sort_sublists(input_list) == expected_output

    def test_multiple_spaces_4(self):
        input_list = []
        expected_output = []
        assert sort_sublists(input_list) == expected_output

    def test_multiple_spaces_5(self):
        input_list = [["carrot", "cat", "cucumber"], ["apple", "apricot"]]
        expected_output = [["carrot", "cat", "cucumber"], ["apple", "apricot"]]
        assert sort_sublists(input_list) == expected_output

    def test_multiple_spaces_6(self):
        input_list = [["Banana", "apple", "cherry"], ["Dog", "cat", "elephant"]]
        expected_output = [["Banana", "apple", "cherry"], ["Dog", "cat", "elephant"]]
        assert sort_sublists(input_list) == expected_output

    def test_multiple_spaces_7(self):
        input_list = [["apple1", "apple2", "apple!"], ["!dog", "2cat", "elephant"]]
        expected_output = [["apple!", "apple1", "apple2"], ["!dog", "2cat", "elephant"]]
        assert sort_sublists(input_list) == expected_output

