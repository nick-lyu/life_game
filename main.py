import os
from time import sleep


from Board import Board


def console_print_game(board, alive_cell_symbol='■', dead_cell_symbol='□'):
    board_to_print = [[alive_cell_symbol if cell.alive else dead_cell_symbol for cell in elem] for elem in board]
    for elem in board_to_print:
        print(*elem)


def console_print_neighbors_board(board):
    for elem in board:
        print(*elem)


def main(n: int, m: int, gens: int):
    clear = lambda: os.system('cls')
    my_game = Board(n, m, rnd=True)

    for i in range(gens):
        clear()
        console_print_game(my_game.current_board)
        my_game.next_gen()
        sleep(0.1)


if __name__ == '__main__':
    while True:
        l, w = [int(i) for i in input("Input length and width of Board:\n").split()]
        g = int(input("Input generation count:\n"))
        if type(l) is not int or type(w) is not int or type(g) is not int:
            print('Game is end.')
        main(l, w, g)
