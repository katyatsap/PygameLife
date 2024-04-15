import random

class GameOfLife:
    def __init__(self, width, height):
        self.field = [[0] * width for i in range(height)]

    def initialize(self, life_fraction):
        # перебираем так, чтобы не задеть крайние полосы
        # тогда все граничные точки всегда будут неживые
        for y in range (1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                if random.randint(1, 100) <= life_fraction:
                    self.field[y][x] = 1

    def run_transition_rule(self):
        # создаем буфетное поле, в котором будем хранить промежуточные состояния
        buffer_field = [[0] * len(self.field[0]) for i in range(len(self.field))]
        # не трогаем крайние клетки, чтобы не проверять границы
        for y in range (1, len(self.field) - 1):
            for x in range (1, len(self.field[0]) - 1):
                # количество живых соседей
                live_neighbors = 0
                # перебираем клетки 3х3, где центральной является клетка x;y
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        # клетка не проверяет сама себя
                        if dx == 0 and dy == 0:
                            continue
                        if self.field[y + dy][x + dx] == 1:
                            live_neighbors += 1
                # правило перехода
                if live_neighbors < 2 or live_neighbors > 3:
                    buffer_field[y][x] = 0
                elif live_neighbors == 3:
                    buffer_field[y][x] = 1
                else:
                    buffer_field[y][x] = self.field[y][x]
        # копируем буферное поле с основного
        for y in range(1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                self.field[y][x] = buffer_field[y][x]

class GameOfLifeHeirOne(GameOfLife):
    def __init__(self, width, height):
        self.field = [[0] * width for i in range(height)]

    def run_transition_rule(self):
        # создаем буфетное поле, в котором будем хранить промежуточные состояния
        buffer_field = [[0] * len(self.field[0]) for i in range(len(self.field))]
        # не трогаем крайние клетки, чтобы не проверять границы
        for y in range (1, len(self.field) - 1):
            for x in range (1, len(self.field[0]) - 1):
                # количество живых соседей
                live_neighbors = 0
                # перебираем клетки 3х3, где центральной является клетка x;y
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        # клетка не проверяет сама себя
                        if dx == 0 and dy == 0:
                            continue
                        if self.field[y + dy][x + dx] == 1:
                            live_neighbors += 1
                # правило перехода
                if live_neighbors == 0 or live_neighbors > 5:
                    buffer_field[y][x] = 0
                elif live_neighbors == 3:
                    buffer_field[y][x] = 1
                else:
                    buffer_field[y][x] = self.field[y][x]
        # копируем буферное поле с основного
        for y in range(1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                self.field[y][x] = buffer_field[y][x]

class GameOfLifeHeirTwo(GameOfLife):
    def __init__(self, width, height):
        self.field = [[0] * width for i in range(height)]

    def run_transition_rule(self):
        # создаем буфетное поле, в котором будем хранить промежуточные состояния
        buffer_field = [[0] * len(self.field[0]) for i in range(len(self.field))]
        # не трогаем крайние клетки, чтобы не проверять границы
        for y in range (1, len(self.field) - 1):
            for x in range (1, len(self.field[0]) - 1):
                # количество живых соседей
                live_neighbors = 0
                # перебираем клетки 3х3, где центральной является клетка x;y
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        # клетка не проверяет сама себя
                        if dx == 0 and dy == 0:
                            continue
                        if self.field[y + dy][x + dx] == 1:
                            live_neighbors += 1
                # правило перехода
                if live_neighbors <= 1 or live_neighbors >= 5:
                    buffer_field[y][x] = 0
                elif live_neighbors >= 2 or live_neighbors <= 4:
                    buffer_field[y][x] = 1
                else:
                    buffer_field[y][x] = self.field[y][x]
        # копируем буферное поле с основного
        for y in range(1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                self.field[y][x] = buffer_field[y][x]