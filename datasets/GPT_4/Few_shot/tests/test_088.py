import unittest
from datasets.GPT_4.Few_shot.programs.program_088 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(round(area_polygon(5, 3), 2), 10.83) # Triangle with side length 5)

    def test_case_2(self):
        self.assertEqual(round(area_polygon(4, 4), 2), 16.00) # Square with side length 4)

    def test_case_3(self):
        self.assertEqual(round(area_polygon(2, 6), 2), 10.39) # Hexagon with side length 2)

    def test_case_4(self):
        self.assertEqual(round(area_polygon(1, 8), 2), 4.83) # Octagon with side length 1)

    def test_case_5(self):
        self.assertEqual(round(area_polygon(10, 3), 2), 43.30) # Triangle with side length 10)

    def test_case_6(self):
        self.assertEqual(round(area_polygon(3, 5), 2), 15.48) # Pentagon with side length 3)

    def test_case_7(self):
        self.assertEqual(round(area_polygon(7, 12), 2), 237.76) # Dodecagon with side length 7)

    def test_case_8(self):
        try:
            area_polygon(5, 2)   # Invalid n (polygon must have at least 3 sides)
        except ValueError:
            print("Passed: ValueError for invalid n.")


