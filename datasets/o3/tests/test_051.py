import unittest
from datasets.o3.programs.program_051 import *

class TestVersion(unittest.TestCase):
    def test_base_case_n_zero(self):
        self.assertEqual(eulerian_num(0, 0), 0)

    def test_m_equal_n(self):
        self.assertEqual(eulerian_num(3, 3), 0)

    def test_m_zero(self):
        self.assertEqual(eulerian_num(5, 0), 1)

    def test_small_known_value(self):
        self.assertEqual(eulerian_num(3, 1), 4)

    def test_symmetric_value(self):
        self.assertEqual(eulerian_num(4, 2), 11)

    def test_large_input(self):
        self.assertEqual(eulerian_num(5, 3), 26)

