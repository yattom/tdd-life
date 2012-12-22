# coding: utf8

import unittest

from life import *

def fill_neighbours(cell, alive):
    cell.neighbours = [Cell() for i in range(8)]
    for i in range(alive):
        cell.neighbours[i].live()

def pattern(pattern_with_spaces):
    return '\n'.join([line.strip() for line in pattern_with_spaces.split('\n')])

class CellTest(unittest.TestCase):
    def test_self_state_initial(self):
        cell = Cell()
        self.assertFalse(cell.is_alive())

    def test_self_state_alive(self):
        cell = Cell()
        cell.live()
        self.assertTrue(cell.is_alive())

    def test_knows_neighbours(self):
        cell = Cell()
        another_cell = Cell()
        cell.neighbours.append(another_cell)

        self.assertTrue(another_cell in cell.neighbours)

    def test_next_generation_when_born(self):
        cell = Cell()
        cell.born()

        self.assertFalse(cell.is_alive())
        cell.tick()
        self.assertTrue(cell.is_alive())

    def test_will_born_true(self):
        cell = Cell()
        fill_neighbours(cell, alive=3)
        self.assertTrue(cell.will_born())

    def test_will_born_false(self):
        cell = Cell()
        fill_neighbours(cell, alive=4)
        self.assertFalse(cell.will_born())

class GameOfLifeTest(unittest.TestCase):
    def test_set_initial_pattern(self):
        initial = '''
            oo.
            o..
            ...
'''
        game = GameOfLife(pattern=pattern(initial))

        expected = '''
            oo.
            o..
            ...
'''
        actual = game.dump()
        self.assertEqual(actual, pattern(expected))

    def test_born(self):
        initial = '''
            oo.
            o..
            ...
'''
        game = GameOfLife(pattern=pattern(initial))
        game.tick()

        expected = '''
            oo.
            oo.
            ...
'''
        actual = game.dump()
        self.assertEqual(actual, pattern(expected))

    def test_prepare_next_generation(self):
        game = GameOfLife()
        cell = Cell()
        fill_neighbours(cell, alive=3)
        game.prepare_next_generation([cell])

        cell.tick()
        self.assertTrue(cell.is_alive())

    def test_build_cells(self):
        initial = '''
            oo.
            o..
            ...
'''
        cells = GameOfLife.build_cells(pattern(initial))
        expected = {
            (0, 0): True,  (1, 0): True,  (2, 0): False,
            (0, 1): True,  (1, 1): False, (2, 1): False,
            (0, 2): False, (1, 2): False, (2, 2): False,
        }
        actual = { pos:cells[pos].is_alive() for pos in cells.keys() }
        self.assertEqual(actual, expected)

    def test_connect_neighbours(self):
        cells = {
            (0, 0): Cell(), (1, 0): Cell(), (2, 0): Cell(),
            (0, 1): Cell(), (1, 1): Cell(), (2, 1): Cell(),
            (0, 2): Cell(), (1, 2): Cell(), (2, 2): Cell(),
        }
        GameOfLife.connect_neighbours(cells)
        self.assertEqual(sorted(cells[(0, 0)].neighbours),
            sorted([cells[(1, 0)], cells[(0, 1)], cells[(1, 1)]]))

        self.assertEqual(sorted(cells[(1, 1)].neighbours),
            sorted([
                cells[(0, 0)], cells[(1, 0)], cells[(2, 0)],
                cells[(0, 1)],                cells[(2, 1)],
                cells[(0, 2)], cells[(1, 2)], cells[(2, 2)],
            ]))

    def test_dump_cells(self):
        cells = {
            (0, 0): Cell(), (1, 0): Cell(), (2, 0): Cell(),
            (0, 1): Cell(), (1, 1): Cell(), (2, 1): Cell(),
            (0, 2): Cell(), (1, 2): Cell(), (2, 2): Cell(),
        }
        cells[(0, 0)].live()
        cells[(0, 2)].live()
        cells[(2, 1)].live()
        expected = '''
            o..
            ..o
            o..
'''
        actual = GameOfLife.dump_cells(cells)
        self.assertEqual(actual, pattern(expected))

if __name__=='__main__':
    unittest.main()
