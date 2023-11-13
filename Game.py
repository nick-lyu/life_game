from Cell import Cell


class Game:

    def __init__(self, n, m, rnd=False):
        if rnd:
            self.current_board = [[Cell(rnd_alive=True) for j in range(n)] for i in range(m)]
        else:
            self.current_board = [[Cell for j in range(n)] for i in range(m)]

    def next_gen(self):
        alive_neighbors_board = self.get_alive_neighbors_board()
        for i in range(len(self.current_board)):
            for j in range(len(self.current_board[i])):
                cell = self.current_board[i][j]
                alive_neighbors = alive_neighbors_board[i][j]
                if cell.alive:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        cell.die()
                        continue
                    continue
                else:
                    if alive_neighbors == 3:
                        cell.born()
        # return self.current_board

    def get_alive_neighbors_board(self):
        alive_neighbors_board = [
            [
                self.get_alive_neighbors(i, j) for j in range(len(self.current_board[i]))
            ] for i in range(len(self.current_board))
        ]
        return alive_neighbors_board

    def get_alive_neighbors(self, x, y):

        alive_count = 0

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if not (i == x and j == y):
                    current_cell = self.current_board[i][j]
                    if current_cell.alive:
                        alive_count += 1
        return alive_count

    def normalize_ranges(self, x, y):
        if x == len(self.current_board) - 1:
            a = 0