from random import choice


colors = ['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', 'pink',
          'purple', 'red', 'yellow', 'violet', 'indigo', 'chartreuse', 'lime']


class Cell:

    def __init__(self):
        self.color = 'blank'

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
