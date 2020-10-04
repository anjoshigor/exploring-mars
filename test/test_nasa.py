import unittest
from model.probe import Probe
from model.land import Land
from controller.nasa import Nasa

class TestNasa(unittest.TestCase):

    def test_move_left_when_facing_north(self):
        probe = Probe(0,0,"N")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertEqual(nasa.move(probe, "L").direction, "W")

    def test_move_left_when_facing_south(self):
        probe = Probe(0,0,"S")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertEqual(nasa.move(probe, "L").direction, "E")

    def test_move_left_when_facing_west(self):
        probe = Probe(0,0,"W")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertEqual(nasa.move(probe, "L").direction, "S")

    def test_move_left_when_facing_east(self):
        probe = Probe(0,0,"E")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertEqual(nasa.move(probe, "L").direction, "N")

    def test_move_right_when_facing_north(self):
        probe = Probe(0,0,"N")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertEqual(nasa.move(probe, "R").direction, "E")

    def test_move_right_when_facing_south(self):
        probe = Probe(0,0,"S")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertEqual(nasa.move(probe, "R").direction, "W")

    def test_move_right_when_facing_west(self):
        probe = Probe(0,0,"W")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertEqual(nasa.move(probe, "R").direction, "N")

    def test_move_right_when_facing_east(self):
        probe = Probe(0,0,"E")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertEqual(nasa.move(probe, "R").direction, "S")

    def test_move_north_out_from_land(self):
        probe = Probe(0,0,"N")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertWarns(UserWarning, nasa.move, probe, "M")
        movedProbe = nasa.move(probe, "M")
        self.assertEqual(movedProbe, probe)

    def test_move_south_out_from_land(self):
        probe = Probe(0,0,"S")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertWarns(UserWarning, nasa.move, probe, "M")
        movedProbe = nasa.move(probe, "M")
        self.assertEqual(movedProbe, probe)

    def test_move_west_out_from_land(self):
        probe = Probe(0,0,"W")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertWarns(UserWarning, nasa.move, probe, "M")
        movedProbe = nasa.move(probe, "M")
        self.assertEqual(movedProbe, probe)

    def test_move_east_out_from_land(self):
        probe = Probe(0,0,"E")
        land = Land(0,0)
        nasa = Nasa(land)
        self.assertWarns(UserWarning, nasa.move, probe, "M")
        movedProbe = nasa.move(probe, "M")
        self.assertEqual(movedProbe, probe)

if __name__ == '__main__':
    unittest.main()