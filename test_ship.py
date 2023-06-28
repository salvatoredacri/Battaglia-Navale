import unittest

from ship_class import Navi

class TestShip(unittest.TestCase):
    def test_consecutive_horizontal_5len_5len_ships_crash(self):
        first_ship = Navi('first', 5, 'o', 0, 'A', None)
        second_ship = Navi('second', 5, 'o', 0, 'F', None)
        self.assertTrue(first_ship.crashes_against(second_ship))

    def test_consecutive_horizontal_5len_1len_ships_crash(self):
        first_ship = Navi('first', 5, 'o', 0, 'A', None)
        second_ship = Navi('second', 1, 'o', 0, 'F', None)
        self.assertTrue(first_ship.crashes_against(second_ship))

    def test_parallel_horizontal_5len_ships_separated_by_one_row_dont_crash(self):
        first_ship = Navi('first', 5, 'o', 3, 'A', None)
        second_ship = Navi('second', 5, 'o', 5, 'F', None)
        self.assertFalse(first_ship.crashes_against(second_ship))

    def test_completely_overlapped_horizontal_5len_ships_crash(self):
        first_ship = Navi('first', 5, 'o', 3, 'C', None)
        second_ship = Navi('second', 5, 'o', 3, 'C', None)
        self.assertTrue(first_ship.crashes_against(second_ship))        

    def test_completely_overlapped_5len_ships_crash(self):
        first_ship = Navi('first', 5, 'o', 3, 'C', None)
        second_ship = Navi('second', 5, 'o', 3, 'C', None)
        self.assertTrue(first_ship.crashes_against(second_ship))        

    def test_partially_overlapped_5len_ships_crash(self):
        first_ship = Navi('first', 5, 'o', 3, 'C', None)
        second_ship = Navi('second', 5, 'o', 3, 'F', None)
        self.assertTrue(first_ship.crashes_against(second_ship))   

    def test_consecutive_vertical_5len_5len_ships_crash(self):
        first_ship = Navi('first', 5, 'v', 0, 'E', None)
        second_ship = Navi('second', 5, 'v', 5, 'E', None)
        self.assertTrue(first_ship.crashes_against(second_ship))

    def test_consecutive_vertical_5len_horizontal_5len_ships_crash(self):
        first_ship = Navi('first', 5, 'v', 0, 'E', None)
        second_ship = Navi('second', 5, 'o', 5, 'F', None)
        self.assertTrue(first_ship.crashes_against(second_ship))

    def test_parallel_adjacent_5len_vertical_ships_crash(self):
        first_ship = Navi('first', 5, 'v', 0, 'E', None)
        second_ship = Navi('second', 5, 'v', 0, 'F', None)
        self.assertTrue(first_ship.crashes_against(second_ship))

    def test_parallel_adjacent_1len_vertical_ships_crash(self):
        first_ship = Navi('first', 1, 'v', 0, 'E', None)
        second_ship = Navi('second', 1, 'v', 0, 'F', None)
        self.assertTrue(first_ship.crashes_against(second_ship))

    def test_parallel_adjacent_1len_vertical_ships_crash(self):
        first_ship = Navi('first', 1, 'v', 0, 'E', None)
        second_ship = Navi('second', 1, 'v', 0, 'F', None)
        self.assertTrue(first_ship.crashes_against(second_ship))

    def test_diagonal_1len_adjacent_ships_crash(self):
        first_ship = Navi('first', 1, 'v', 0, 'E', None)
        second_ship = Navi('second', 1, 'v', 1, 'F', None)
        self.assertTrue(first_ship.crashes_against(second_ship))

    def test_diagonal_1len_non_adjacent_ships_crash(self):
        first_ship = Navi('first', 1, 'v', 0, 'E', None)
        second_ship = Navi('second', 1, 'v', 2, 'G', None)
        self.assertFalse(first_ship.crashes_against(second_ship))

    def test_T_shaped_ships_crash(self):
        first_ship = Navi('first', 5, 'o', 0, 'A', None)
        second_ship = Navi('second', 5, 'v', 1, 'C', None)
        self.assertTrue(first_ship.crashes_against(second_ship))