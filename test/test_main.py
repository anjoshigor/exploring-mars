import unittest
from main import main
from model.probe import Probe
from model.land import Land

class TestMain(unittest.TestCase):

    def test_first_input(self):
        land = Land(5, 5)
        probe = Probe(1, 2,"N")
        result = main(land, probe, "LMLMLMLMM")
        self.assertEqual(result, "1 3 N")

    def test_second_input(self):
        land = Land(5, 5)
        probe = Probe(3, 3,"E")
        result = main(land, probe, "MMRMMRMRRM")
        self.assertEqual(result, "5 1 E")
    
    def test_out_of_mars(self):
        land = Land(5, 5)
        probe = Probe(3, 3,"E")
        result = main(land, probe, "MMRMMRMRRMMMMMMMM")
        self.assertEqual(result, "5 1 E")

    def test_circling(self):
        land = Land(5, 5)
        probe = Probe(3, 3,"E")
        result = main(land, probe, "LLLL")
        self.assertEqual(result, "3 3 E")
  
if __name__ == '__main__':
    unittest.main()