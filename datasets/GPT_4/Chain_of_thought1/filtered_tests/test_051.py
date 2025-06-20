import unittest
from datasets.GPT_4.Chain_of_thought1.programs.program_051 import *

class TestVersion(unittest.TestCase):
    def test_zero_zero(self): self.assertEqual(eulerian_num(0, 0), 0)

    def test_n_zero(self): self.assertEqual(eulerian_num(1, 0), 1); self.assertEqual(eulerian_num(5, 0), 1)

    def test_m_greater_equal_n(self): self.assertEqual(eulerian_num(4, 4), 0); self.assertEqual(eulerian_num(3, 5), 0)

    def test_known_value_2_1(self): self.assertEqual(eulerian_num(2, 1), 1)

    def test_known_value_3_1(self): self.assertEqual(eulerian_num(3, 1), 4)

    def test_known_value_4_1(self): self.assertEqual(eulerian_num(4, 1), 11)

    def test_known_value_4_2(self): self.assertEqual(eulerian_num(4, 2), 11)

    def test_negative_input(self): self.assertEqual(eulerian_num(-1, 2), 0); self.assertEqual(eulerian_num(3, -1), 0)

    def test_large_input(self): result = eulerian_num(7, 3); self.assertIsInstance(result, int); self.assertGreater(result, 0)

