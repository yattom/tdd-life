# coding: utf8

import unittest

from life import *

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

        self.assertTrue(game.isAlive(1, 1))

if __name__=='__main__':
    unittest.main()
