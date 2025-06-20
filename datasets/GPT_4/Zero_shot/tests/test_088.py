import unittest
from datasets.GPT_4.Zero_shot.programs.program_088 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        s = 5
        n = 4
        expected_output = 25.0  # Square with side length 5
        assert area_polygon(s, n) == expected_output

    def test_multiple_spaces_2(self):
        s = 10
        n = 6
        expected_output = 259.8076211353316  # Hexagon with side length 10
        assert area_polygon(s, n) == expected_output

    def test_multiple_spaces_3(self):
        s = 7
        n = 3
        expected_output = 21.21762239271875  # Triangle with side length 7
        assert area_polygon(s, n) == expected_output

    def test_multiple_spaces_4(self):
        s = 1
        n = 100
        expected_output = 0.03183098861837907  # Polygon with 100 sides and side length 1
        assert area_polygon(s, n) == expected_output

    def test_multiple_spaces_5(self):
        s = 5
        n = 2
        try:
            area_polygon(s, n)
            assert False, "Expected a ValueError due to invalid number of sides"
        except ValueError:
            pass  # Assuming the function raises a ValueError for n < 3

    def test_multiple_spaces_6(self):
        s = -4
        n = 5
        try:
            area_polygon(s, n)
            assert False, "Expected a ValueError due to negative side length"
        except ValueError:
            pass  # Assuming the function raises a ValueError for negative side length

    def test_multiple_spaces_7(self):
        s = 1000
        n = 8
        expected_output = 4828427.12474619  # Octagon with side length 1000
        assert area_polygon(s, n) == expected_output

