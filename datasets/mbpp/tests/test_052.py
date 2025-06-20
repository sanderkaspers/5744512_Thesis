import unittest
from datasets.mbpp.programs.program_052 import *

class TestVersion(unittest.TestCase):
    def test_sort_sublists_with__green___orange___black___white___white___black___orange(self):
        self.assertEqual(sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"])), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

    def test_sort_sublists_with__red___green___blue___black___orange___brown__expect__re(self):
        self.assertEqual(sort_sublists(([" red ","green" ],["blue "," black"],[" orange","brown"])), [[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']])

    def test_sort_sublists_with__zilver___gold___magnesium___aluminium___steel___bronze_(self):
        self.assertEqual(sort_sublists((["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"])), [['gold', 'zilver'],['aluminium', 'magnesium'], ['bronze', 'steel']])

