import unittest
from datasets.mbpp.programs.program_030 import *

class TestVersion(unittest.TestCase):
    def test_volume_sphere_with_10_expect_4188_790204786391(self):
        self.assertEqual(volume_sphere(10), 4188.790204786391)

    def test_volume_sphere_with_25_expect_65449_84694978735(self):
        self.assertEqual(volume_sphere(25), 65449.84694978735)

    def test_volume_sphere_with_20_expect_33510_32163829113(self):
        self.assertEqual(volume_sphere(20), 33510.32163829113)

