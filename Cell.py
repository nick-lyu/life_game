from random import choice


colors = ['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', 'pink',
          'purple', 'red', 'yellow', 'violet', 'indigo', 'chartreuse', 'lime']


class Cell:

    def __init__(self, alive=False, rnd_alive=False, rnd_prob=50):
        # self.color = 'blank'
        self.color = 'black'
        self.alive = alive
        if rnd_alive:
            self.alive = choice((True, False))

    def born(self):
        self.alive = True

    def die(self):
        self.alive = False

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def mutation(self):
        self.color = choice(colors)


# mutations:
# mobility
# way of eating
# method of replication (reproduction)
# ability to unite into a multicellular creature
# memory
# color
