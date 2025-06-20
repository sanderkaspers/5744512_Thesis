import unittest
from datasets.GPT_4.Zero_shot.programs.program_030 import *

class TestVersion(unittest.TestCase):
    def test_multiple_spaces(self):
        r = 0
        expected_output = 0.0
        assert volume_sphere(r) == expected_output

    def test_multiple_spaces_2(self):
        r = 1
        expected_output = 4.1887902047863905
        assert volume_sphere(r) == expected_output

    def test_multiple_spaces_3(self):
        r = 10
        expected_output = 4188.790204786391
        assert volume_sphere(r) == expected_output

    def test_multiple_spaces_4(self):
        r = 1000
        expected_output = 4188790204.7863905
        assert volume_sphere(r) == expected_output

    def test_multiple_spaces_5(self):
        r = 2.5
        expected_output = 65.44984694978736
        assert volume_sphere(r) == expected_output

    def test_multiple_spaces_6(self):
        r = -3
        try:
            volume_sphere(r)
            expected_output = None
        except ValueError:
            expected_output = "ValueError"
        assert expected_output == "ValueError"

