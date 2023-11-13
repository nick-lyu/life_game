import os
from time import sleep
from tkinter import Tk, Canvas, Button, Frame, BOTH, NORMAL, HIDDEN

from Game import Game


def console_print_game(board, alive_cell_symbol='■', dead_cell_symbol='□'):
    board_to_print = [[alive_cell_symbol if cell.alive else dead_cell_symbol for cell in elem] for elem in board]
    for elem in board_to_print:
        print(*elem)


def console_print_neighbors_board(board):
    for elem in board:
        print(*elem)

def main():
    clear = lambda: os.system('clear')
    my_game = Game(5, 5, rnd=True)
    gens = 10
    console_print_game(my_game.current_board)
    console_print_neighbors_board(my_game.get_alive_neighbors_board())

    # for i in range(gens):
    #     my_game.next_gen()
    #     # clear()
    #     print()
    #     console_print_game(my_game.current_board)
    #     # sleep(1)


if __name__ == '__main__':
    # main()
    a = [i for i in range(4)]
    b = a[2:1]
    print(a)
    print(b)
