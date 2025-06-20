import unittest
from datasets.GPT_4.Few_shot.programs.program_033 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(surfacearea_sphere(1), 4 * math.pi) # Unit sphere)

    def test_case_2(self):
        self.assertEqual(surfacearea_sphere(0), 0) # Zero radius)

    def test_case_3(self):
        self.assertEqual(surfacearea_sphere(3), 4 * math.pi * (3**2) )  # Normal positive radius)

    def test_case_4(self):
        self.assertEqual(surfacearea_sphere(-3), 4 * math.pi * (3**2))   # Negative radius (absolute value used))

    def test_case_5(self):
        self.assertEqual(surfacearea_sphere(10), 4 * math.pi * (10**2))   # Large radius)

    def test_case_6(self):
        self.assertEqual(surfacearea_sphere(0.5), 4 * math.pi * (0.5**2))   # Fractional radius)

    def test_case_7(self):
        self.assertEqual(surfacearea_sphere(2.5), 4 * math.pi * (2.5**2))   # Another fractional radius)

    def test_case_8(self):
        self.assertEqual(surfacearea_sphere(100), 4 * math.pi * (100**2))   # Very large radius))

