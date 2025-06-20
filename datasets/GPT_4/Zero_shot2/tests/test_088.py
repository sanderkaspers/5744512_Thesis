import unittest
from datasets.GPT_4.Zero_shot2.programs.program_088 import *

class TestVersion(unittest.TestCase):
    def test_poly_1(self):
        self.assertAlmostEqual(area_polygon(3, 1), 0.43301270189221946)

    def test_poly_2(self):
        self.assertAlmostEqual(area_polygon(4, 1), 1.0000000000000002)

    def test_poly_3(self):
        self.assertAlmostEqual(area_polygon(5, 1), 1.720477400588967)

    def test_poly_4(self):
        self.assertAlmostEqual(area_polygon(1000, 1), 79577.47154594767)

    def test_poly_5(self):
        self.assertAlmostEqual(area_polygon(4, -1), 1.0000000000000002)

    def test_poly_6(self):
        self.assertAlmostEqual(area_polygon(4, 0), 0.0)

    def test_poly_7(self):
        self.assertAlmostEqual(area_polygon(6, 1.5), 2.598076211353316)

    def test_poly_8(self):
        self.assertAlmostEqual(area_polygon(4, 0.0001), 2.5000000000000004e-09)

    def test_poly_9(self):
        self.assertAlmostEqual(area_polygon(6, 10000), 259807621.1353316)

