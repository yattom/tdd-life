# coding: utf8

class GameOfLife(object):
    def __init__(self, pattern):
        self.pattern = pattern

    def dump(self):
        return self.pattern

    def prepare_next_generation(self, cells):
        for cell in cells:
            if cell.will_born():
                cell.born()

    @staticmethod
    def build_cells(pattern):
        cells = {}
        for y, line in enumerate(pattern.strip().split("\n")):
            for x, c in enumerate(line.strip()):
                if c == 'o':   state = Cell.ALIVE
                elif c == '.': state = Cell.DEAD
                cells[(x, y)] = Cell(state)
        return cells


class Cell(object):
    ALIVE = True
    DEAD = False

    def __init__(self, state=DEAD):
        self.state = state
        self.neighbours = []

    def is_alive(self):
        return self.state == Cell.ALIVE

    def live(self):
        self.state = Cell.ALIVE

    def born(self):
        self.next_state = Cell.ALIVE

    def tick(self):
        self.state = self.next_state

    def will_born(self):
        alive_cells = 0
        for cell in self.neighbours:
            if cell.is_alive():
                alive_cells += 1
        return alive_cells == 3

