import unittest
from datasets.mbpp.programs.program_006 import *

class TestVersion(unittest.TestCase):
    def test_remove_dirty_chars_with__probasscurve___pros__expect_bacuve(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), "bacuve")

    def test_remove_dirty_chars_with__digitalindia___talent__expect_digiidi(self):
        self.assertEqual(remove_dirty_chars("digitalindia", "talent"), "digiidi")

    def test_remove_dirty_chars_with__exoticmiles___toxic__expect_emles(self):
        self.assertEqual(remove_dirty_chars("exoticmiles", "toxic"), "emles")

