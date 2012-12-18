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

    def test_will_born_true(self):
        cell = Cell()
        cell.neighbours = [Cell() for i in range(8)]
        cell.neighbours[0].live()
        cell.neighbours[1].live()
        cell.neighbours[2].live()
        self.assertTrue(cell.will_born())

    def test_will_born_false(self):
        cell = Cell()
        cell.neighbours = [Cell() for i in range(8)]
        cell.neighbours[0].live()
        cell.neighbours[1].live()
        cell.neighbours[2].live()
        cell.neighbours[3].live()
        self.assertFalse(cell.will_born())

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

    def test_prepare_next_generation(self):
        game = GameOfLife(pattern=None)
        class CellStub(object):
            born_is_called = False
            def will_born(self): return True
            def born(self): self.born_is_called = True

        cells = [CellStub()]
        game.prepare_next_generation(cells)
        self.assertTrue(cells[0].born_is_called)

if __name__=='__main__':
    unittest.main()
