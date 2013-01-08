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
    def setUp(self):
        self.cell = Cell()

    def test_self_state_initial(self):
        self.assertFalse(self.cell.is_alive())

    def test_self_state_alive(self):
        self.cell.live()
        self.assertTrue(self.cell.is_alive())

    def test_knows_neighbours(self):
        another_cell = Cell()
        self.cell.neighbours.append(another_cell)

        self.assertTrue(another_cell in self.cell.neighbours)

    def test_next_generation_when_born(self):
        self.cell.born()

        self.assertFalse(self.cell.is_alive())
        self.cell.tick()
        self.assertTrue(self.cell.is_alive())

    def test_will_born_true(self):
        fill_neighbours(self.cell, alive=3)
        self.assertTrue(self.cell.will_born())

    def test_will_born_false(self):
        fill_neighbours(self.cell, alive=4)
        self.assertFalse(self.cell.will_born())

class GameOfLifeTest(unittest.TestCase):
    def assert_next_generation(self, current, expected_next):
        game = GameBuilder.build_with(pattern=pattern(current))
        game.tick()
        actual = GameDumper.dump(game)
        self.assertEqual(actual, pattern(expected_next), 'next generation differs\nexpected:\n%s\nactual:\n%s'%(pattern(expected_next), actual))

    def test_born(self):
        initial = '''
            oo.
            o..
            ...
'''
        expected = '''
            oo.
            oo.
            ...
'''
        self.assert_next_generation(initial, expected)

    def test_prepare_next_generation(self):
        game = GameOfLife(cells={})
        cell = Cell()
        fill_neighbours(cell, alive=3)
        game.prepare_next_generation([cell])

        cell.tick()
        self.assertTrue(cell.is_alive())



class GameBuilderTest(unittest.TestCase):
    def test_build_cells(self):
        initial = '''
            oo.
            o..
            ...
'''
        game = GameBuilder.build_with(initial)
        expected = {
            (0, 0): True,  (1, 0): True,  (2, 0): False,
            (0, 1): True,  (1, 1): False, (2, 1): False,
            (0, 2): False, (1, 2): False, (2, 2): False,
        }
        actual = { pos:game.cells[pos].is_alive() for pos in game.cells.keys() }
        self.assertEqual(actual, expected)

    def test_build_cells(self):
        initial = '''
            oo.
            o..
            ...
'''
        cells = GameBuilder.build_cells(pattern(initial))
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
        GameBuilder.connect_neighbours(cells)
        self.assertEqual(sorted(cells[(0, 0)].neighbours),
            sorted([
                               cells[(1, 0)],
                cells[(0, 1)], cells[(1, 1)]
            ]))

        self.assertEqual(sorted(cells[(1, 1)].neighbours),
            sorted([
                cells[(0, 0)], cells[(1, 0)], cells[(2, 0)],
                cells[(0, 1)],                cells[(2, 1)],
                cells[(0, 2)], cells[(1, 2)], cells[(2, 2)],
            ]))

class GameDumperTest(unittest.TestCase):
    def test_dump(self):
        cell_states = {
            (0, 0): True,  (1, 0): False, (2, 0): False,
            (0, 1): False, (1, 1): False, (2, 1): True,
            (0, 2): True,  (1, 2): False, (2, 2): False,
        }
        cells = { pos:Cell(state=cell_states[pos]) for pos in cell_states.keys() }
        game = GameOfLife(cells=cells)
        expected = '''
            o..
            ..o
            o..
'''
        actual = GameDumper.dump(game)
        self.assertEqual(actual, pattern(expected))


if __name__=='__main__':
    unittest.main()
