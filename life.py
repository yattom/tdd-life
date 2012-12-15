# coding: utf8

class GameOfLife(object):
    def __init__(self, pattern):
        self.pattern = pattern

    def dump(self):
        return self.pattern

    def prepare_next_generation(self, cells):
        for cell in cells:
            if self.will_born(cell.neighbours):
                cell.born()

    def will_born(self, neighbours):
        alive_cells = 0
        for cell in neighbours:
            if cell.is_alive():
                alive_cells += 1
        return alive_cells == 3
