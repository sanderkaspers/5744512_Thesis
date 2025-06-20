import unittest
import pytest
from datasets.pynguin.programs import program_077 as module_0

class TestAll(unittest.TestCase):
    def test_case_0(self):
        bytes_0 = b'\xeaW>\x00\xf9\xcf\xa0HQ\x07\xae"N\x06i'
        var_0 = module_0.zero_count(bytes_0)
        assert var_0 == pytest.approx(0.07142857142857142, abs=0.01, rel=0.01)

