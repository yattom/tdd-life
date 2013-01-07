# coding: utf8

class GameOfLife(object):
    def __init__(self, pattern=''):
        self.cells = GameOfLife.build_cells(pattern)
        GameOfLife.connect_neighbours(self.cells)

    def dump(self):
        return GameOfLife.dump_cells(self.cells)

    def tick(self):
        self.prepare_next_generation(self.cells.values())
        for cell in self.cells.values(): cell.tick()

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

    NEIGHBOUR_POSITIONS = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if not dx == dy == 0]
    @staticmethod
    def connect_neighbours(cells):
        for x, y in cells.keys():
            GameOfLife.connect_neighbour(cells[(x, y)], x, y, cells)

    @staticmethod
    def connect_neighbour(cell, x, y, cells):
        for dx, dy in GameOfLife.NEIGHBOUR_POSITIONS:
            if (x + dx, y + dy) not in cells: continue
            cell.neighbours.append(cells[(x + dx, y + dy)])

    @staticmethod
    def dump_cells(cells):
        grid_max = max(cells.keys())
        dump = [[''] * (grid_max[0] + 1) for i in range(grid_max[1] + 1)]
        for x, y in cells.keys():
            if cells[(x, y)].is_alive(): c = 'o'
            else: c = '.'
            dump[y][x] = c
        return '\n' + '\n'.join([''.join(line) for line in dump]) + '\n'


class Cell(object):
    ALIVE = True
    DEAD = False

    def __init__(self, state=DEAD):
        self.next_state = self.state = state
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

class GameBuilder(object):
    @staticmethod
    def build_with(pattern):
        cells = GameBuilder.build_cells(pattern)

        GameOfLife.connect_neighbours(cells)
        game = GameOfLife()
        game.cells = cells

        return game

    @staticmethod
    def build_cells(pattern):
        cells = {}
        for y, line in enumerate(pattern.strip().split("\n")):
            for x, c in enumerate(line.strip()):
                if c == 'o':   state = Cell.ALIVE
                elif c == '.': state = Cell.DEAD
                cells[(x, y)] = Cell(state)
        return cells

