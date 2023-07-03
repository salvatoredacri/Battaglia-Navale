import unittest

from ship_class import Navi, OrientamentoNave

class TestShipCrash(unittest.TestCase):
    def test_two_horizontal_consecutive_ships_crash(self):
        """
            A B C D E F G H I
          1 > > > > > < 0 0 0
          2 0 0 0 0 0 0 0 0 0
          3 0 0 0 0 0 0 0 0 0
          4 0 0 0 0 0 0 0 0 0
          5 0 0 0 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first = Navi("first", 5, 'o', 0, 'A', None)
        second = Navi("second", 1, 'o', 0, 'F', None)
        self.assertTrue(first.crashes_against(second))

    def test_two_horizontal_ships_separated_by_one_cell_dont_crash(self):
        """
            A B C D E F G H I
          1 > > > > > 0 < 0 0
          2 0 0 0 0 0 0 0 0 0
          3 0 0 0 0 0 0 0 0 0
          4 0 0 0 0 0 0 0 0 0
          5 0 0 0 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first = Navi("first", 5, 'o', 0, 'A', None)
        second = Navi("second", 2, 'o', 0, 'G', None)
        self.assertFalse(first.crashes_against(second))

    def test_two_adjacent_horizontal_parallel_ships_crash(self):
        """
            A B C D E F G H I
          1 > > > > > 0 0 0 0
          2 < < < < < 0 0 0 0
          3 0 0 0 0 0 0 0 0 0
          4 0 0 0 0 0 0 0 0 0
          5 0 0 0 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first = Navi("first", 5, 'o', 0, 'A', None)
        second = Navi("second", 5, 'o', 1, 'A', None)
        self.assertTrue(first.crashes_against(second))

    def test_two_horizontal_parallel_ships_separated_by_one_row_dont_crash(self):
        """
            A B C D E F G H I
          1 > > > > > 0 0 0 0
          2 0 0 0 0 0 0 0 0 0
          3 < < < < < 0 0 0 0
          4 0 0 0 0 0 0 0 0 0
          5 0 0 0 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first = Navi("first", 5, 'o', 0, 'A', None)
        second = Navi("second", 5, 'o', 2, 'A', None)
        self.assertFalse(first.crashes_against(second))

    def test_two_diagonal_1len_ships_crash(self):
        """
            A B C D E F G H I
          1 > 0 0 0 0 0 0 0 0
          2 0 < 0 0 0 0 0 0 0
          3 0 0 0 0 0 0 0 0 0
          4 0 0 0 0 0 0 0 0 0
          5 0 0 0 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first = Navi("first", 1, 'o', 0, 'A', None)
        second = Navi("second", 1, 'o', 1, 'B', None)
        self.assertTrue(first.crashes_against(second))

    def test_two_T_shaped_ships_crash(self):
        """
            A B C D E F G H I
          1 > > > > > 0 0 0 0
          2 0 0 < 0 0 0 0 0 0
          3 0 0 < 0 0 0 0 0 0
          4 0 0 < 0 0 0 0 0 0
          5 0 0 < 0 0 0 0 0 0
          6 0 0 < 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first = Navi("first", 5, 'o', 0, 'A', None)
        second = Navi("second", 5, 'v', 1, 'C', None)
        self.assertTrue(first.crashes_against(second))

    def test_two_vertical_consecutive_ships_crash(self):
        """
            A B C D E F G H I
          1 > 0 0 0 0 0 0 0 0
          2 > 0 0 0 0 0 0 0 0
          3 > 0 0 0 0 0 0 0 0
          4 > 0 0 0 0 0 0 0 0
          5 > 0 0 0 0 0 0 0 0
          6 < 0 0 0 0 0 0 0 0
          7 < 0 0 0 0 0 0 0 0
          8 < 0 0 0 0 0 0 0 0
          9 < 0 0 0 0 0 0 0 0
        """
        first = Navi("first", 5, 'v', 0, 'A', None)
        second = Navi("second", 4, 'v', 5, 'A', None)
        self.assertTrue(first.crashes_against(second))

    def test_two_vertical_consecutive_ships_separated_by_one_cell_dont_crash(self):
        """
            A B C D E F G H I
          1 > 0 0 0 0 0 0 0 0
          2 > 0 0 0 0 0 0 0 0
          3 > 0 0 0 0 0 0 0 0
          4 > 0 0 0 0 0 0 0 0
          5 > 0 0 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 < 0 0 0 0 0 0 0 0
          8 < 0 0 0 0 0 0 0 0
          9 < 0 0 0 0 0 0 0 0
        """
        first = Navi("first", 5, 'v', 0, 'A', None)
        second = Navi("second", 3, 'v', 6, 'A', None)
        self.assertFalse(first.crashes_against(second))

    def test_two_adjacent_vertical_parallel_ships_crash(self):
        """
            A B C D E F G H I
          1 > < 0 0 0 0 0 0 0
          2 > < 0 0 0 0 0 0 0
          3 > < 0 0 0 0 0 0 0
          4 > < 0 0 0 0 0 0 0
          5 > < 0 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first = Navi("first", 5, 'v', 0, 'A', None)
        second = Navi("second", 5, 'v', 0, 'B', None)
        self.assertTrue(first.crashes_against(second))

    def test_two_vertical_parallel_ships_separated_by_one_col_dont_crash(self):
        """
            A B C D E F G H I
          1 > 0 < 0 0 0 0 0 0
          2 > 0 < 0 0 0 0 0 0
          3 > 0 < 0 0 0 0 0 0
          4 > 0 < 0 0 0 0 0 0
          5 > 0 < 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first = Navi("first", 5, 'v', 0, 'A', None)
        second = Navi("second", 5, 'v', 0, 'C', None)
        self.assertFalse(first.crashes_against(second))

    def test_completely_overlapped_horizontal_5len_ships_crash(self):
        """
            A B C D E F G H I
          1 0 0 0 0 0 0 0 0 0
          2 0 0 0 0 0 0 0 0 0
          3 0 0 x x x x x 0 0
          4 0 0 0 0 0 0 0 0 0
          5 0 0 0 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first_ship = Navi('first', 5, 'o', 2, 'C', None)
        second_ship = Navi('second', 5, 'o', 2, 'C', None)
        self.assertTrue(first_ship.crashes_against(second_ship))        

    def test_partially_overlapped_5len_ships_crash(self):
        """
            A B C D E F G H I
          1 0 0 0 0 0 0 0 0 0
          2 0 0 0 0 0 0 0 0 0
          3 0 > > > x x < < <
          4 0 0 0 0 0 0 0 0 0
          5 0 0 0 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first_ship = Navi('first', 5, 'o', 2, 'B', None)
        second_ship = Navi('second', 5, 'o', 2, 'E', None)
        self.assertTrue(first_ship.crashes_against(second_ship))   

    def test_L_shaped_ships_crash(self):
        """
            A B C D E F G H I
          1 0 0 0 0 > 0 0 0 0
          2 0 0 0 0 > 0 0 0 0
          3 0 0 0 0 > 0 0 0 0
          4 0 0 0 0 > 0 0 0 0
          5 0 0 0 0 > < < < <
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first_ship = Navi('first', 5, 'v', 0, 'E', None)
        second_ship = Navi('second', 4, 'o', 4, 'F', None)
        self.assertTrue(first_ship.crashes_against(second_ship))

    def test_parallel_adjacent_1len_vertical_ships_crash(self):
        """
            A B C D E F G H I
          1 0 0 0 0 > < 0 0 0
          2 0 0 0 0 0 0 0 0 0
          3 0 0 0 0 0 0 0 0 0
          4 0 0 0 0 0 0 0 0 0
          5 0 0 0 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first_ship = Navi('first', 1, 'v', 0, 'E', None)
        second_ship = Navi('second', 1, 'v', 0, 'F', None)
        self.assertTrue(first_ship.crashes_against(second_ship))

    def test_diagonal_1len_non_adjacent_vertical_ships_dont_crash(self):
        """
            A B C D E F G H I
          1 0 0 0 0 > 0 0 0 0
          2 0 0 0 0 0 0 0 0 0
          3 0 0 0 0 0 0 < 0 0
          4 0 0 0 0 0 0 0 0 0
          5 0 0 0 0 0 0 0 0 0
          6 0 0 0 0 0 0 0 0 0
          7 0 0 0 0 0 0 0 0 0
          8 0 0 0 0 0 0 0 0 0
          9 0 0 0 0 0 0 0 0 0
        """
        first_ship = Navi('first', 1, 'v', 0, 'E', None)
        second_ship = Navi('second', 1, 'v', 2, 'G', None)
        self.assertFalse(first_ship.crashes_against(second_ship))