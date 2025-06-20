import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_051 import *

class TestVersion(unittest.TestCase):
    def test_base_case_n_zero(self): self.assertEqual(eulerian_num(0, 0), 0); self.assertEqual(eulerian_num(0, 1), 0)

    def test_base_case_m_zero(self): self.assertEqual(eulerian_num(1, 0), 1); self.assertEqual(eulerian_num(2, 0), 1); self.assertEqual(eulerian_num(5, 0), 1)

    def test_m_greater_than_equal_n(self): self.assertEqual(eulerian_num(3, 3), 0); self.assertEqual(eulerian_num(4, 5), 0)

    def test_known_small_values(self): self.assertEqual(eulerian_num(3, 1), 4); self.assertEqual(eulerian_num(4, 2), 11)

    def test_m_equals_n_minus_1(self): self.assertEqual(eulerian_num(4, 3), 1)

    def test_large_inputs(self): self.assertEqual(eulerian_num(7, 3), 302)

    def test_negative_inputs(self): self.assertEqual(eulerian_num(-1, 0), 0); self.assertEqual(eulerian_num(3, -1), 0)

