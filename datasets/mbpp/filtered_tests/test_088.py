import unittest
from datasets.mbpp.programs.program_088 import *

class TestVersion(unittest.TestCase):
    def test_area_polygon_with_4_20_expect_400_00000000000006(self):
        self.assertEqual(area_polygon(4,20), 400.00000000000006)

    def test_area_polygon_with_10_15_expect_1731_1969896610804(self):
        self.assertEqual(area_polygon(10,15), 1731.1969896610804)

    def test_area_polygon_with_9_7_expect_302_90938549487214(self):
        self.assertEqual(area_polygon(9,7), 302.90938549487214)

