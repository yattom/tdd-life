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

if __name__=='__main__':
    unittest.main()
