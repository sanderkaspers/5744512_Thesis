import unittest
from datasets.GPT_4.Zero_shot2.programs.program_085 import *

class TestVersion(unittest.TestCase):
    def test_sol_1(self):
        self.assertTrue(find_solution(3, 5, 11))

    def test_sol_2(self):
        self.assertFalse(find_solution(4, 6, 7))

    def test_sol_3(self):
        self.assertTrue(find_solution(1, 1, 0))

    def test_sol_4(self):
        self.assertTrue(find_solution(0, 5, 10))

    def test_sol_5(self):
        self.assertTrue(find_solution(1, 1, 10))

    def test_sol_6(self):
        self.assertTrue(find_solution(7, 11, 1000))

    def test_sol_7(self):
        self.assertTrue(find_solution(4, 4, 8))

    def test_sol_8(self):
        self.assertFalse(find_solution(10, 20, 5))

    def test_sol_9(self):
        self.assertFalse(find_solution(-3, 5, 15))

    def test_sol_10(self):
        self.assertTrue(find_solution(5, 3, 10))

    def test_sol_11(self):
        self.assertTrue(find_solution(3, 5, 10))

