# coding: utf8

import unittest

from life import *

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

class GameOfLifeTest(unittest.TestCase):
    def test_set_initial_pattern(self):
        initial = '''
oo.
o..
...
'''
        game = GameOfLife(pattern=initial)

        expected = '''
oo.
o..
...
'''
        actual = game.dump()
        self.assertEqual(actual, expected)

    def test_born(self):
        initial = '''
oo.
o..
...
'''
        game = GameOfLife(pattern=initial)
        game.tick()

        expected = '''
oo.
oo.
...
'''
        actual = game.dump()
        self.assertEqual(actual, expected)

    def test_will_born_true(self):
        game = GameOfLife(pattern='')

        cells = [Cell() for i in range(8)]
        cells[0].live()
        cells[1].live()
        cells[2].live()
        self.assertTrue(game.will_born(cells))

    def test_will_born_false(self):
        game = GameOfLife(pattern='')

        cells = [Cell() for i in range(8)]
        cells[0].live()
        cells[1].live()
        cells[2].live()
        cells[3].live()
        self.assertFalse(game.will_born(cells))

if __name__=='__main__':
    unittest.main()
