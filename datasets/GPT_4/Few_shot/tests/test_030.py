import unittest
from datasets.GPT_4.Few_shot.programs.program_030 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(volume_sphere(1), (4/3) * math.pi) # Unit sphere)

    def test_case_2(self):
        self.assertEqual(volume_sphere(0), 0) # Zero radius)

    def test_case_3(self):
        self.assertEqual(volume_sphere(3), (4/3) * math.pi * (3**3))   # Normal positive radius)

    def test_case_4(self):
        self.assertEqual(volume_sphere(-3), -(4/3) * math.pi * (3**3))   # Negative radius)

    def test_case_5(self):
        self.assertEqual(volume_sphere(10), (4/3) * math.pi * (10**3) )  # Large radius))

    def test_case_6(self):
        self.assertEqual(volume_sphere(0.5), (4/3) * math.pi * (0.5**3))   # Fractional radius))

    def test_case_7(self):
        self.assertEqual(volume_sphere(2.5), (4/3) * math.pi * (2.5**3))   # Another fractional radius))

    def test_case_8(self):
        self.assertEqual(volume_sphere(100), (4/3) * math.pi * (100**3))   # Very large radius)

