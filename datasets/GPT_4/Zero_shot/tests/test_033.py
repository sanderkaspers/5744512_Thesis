import unittest
from datasets.GPT_4.Zero_shot.programs.program_033 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        r = 0
        expected_output = 0.0
        assert surfacearea_sphere(r) == expected_output

    def test_multiple_spaces_2(self):
        r = 1
        expected_output = 12.566370614359172
        assert surfacearea_sphere(r) == expected_output

    def test_multiple_spaces_3(self):
        r = 10
        expected_output = 1256.6370614359173
        assert surfacearea_sphere(r) == expected_output

    def test_multiple_spaces_4(self):
        r = 1000
        expected_output = 12566370.614359172
        assert surfacearea_sphere(r) == expected_output

    def test_multiple_spaces_5(self):
        r = 2.5
        expected_output = 78.53981633974483
        assert surfacearea_sphere(r) == expected_output

    def test_multiple_spaces_6(self):
        r = -3
        try:
            surfacearea_sphere(r)
            expected_output = None
        except ValueError:
            expected_output = "ValueError"
        assert expected_output == "ValueError"

