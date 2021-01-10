import copy
import random
from tkinter import *
import time
import re
global black_goal, white_goal, settings
all_defined_boards, all_kill_moves, winner = {}, {}, []
tk = Tk()
random.seed(a=None, version=2)
white_choices = {
    0: {
        'move': [(-1, -1), (1, -1), (-2, -2), (2, -2)]
        },
    1: {
        'move': [(-1, -1), (1, -1), (-1, 1), (1, 1), (-2, -2), (2, -2), (-2, 2), (2, 2)]
        }
}
black_choices = {
    0: {
        'move': [(-1, 1), (1, 1), (-2, 2), (2, 2)]
        },
    1: {
        'move': [(-1, -1), (1, -1), (-1, 1), (1, 1), (-2, -2), (2, -2), (-2, 2), (2, 2)]
        }
}


def build_board():
    white_team, black_team = {}, {}
    board, coordinated_board = [], []
    coding_board = ''
    z_row = 0
    for y in reversed(range(8)):
        z = z_row
        if z == 0:
            z_row = 1
        else:
            z_row = 0
        board_row, coordinated_board_row = [], []
        for x in range(8):
            board_row.append(str(z))
            coordinated_board_row.append((x, y))
            if z == 0:
                z = 1
            else:
                z = 0
        board.append(board_row)
        coordinated_board.append(coordinated_board_row)
    loose_board = copy.deepcopy(board)
    # [print('  '.join(i)) for i in board]
    # print('\n')
    for i in range(3):
        for k, j in enumerate(board[i]):
            if j == '1':
                board[i][k] = 'w'
                white_team.update({coordinated_board[i][k]: 0})
    for i in reversed(range(5, 8)):
        for k, j in enumerate(board[i]):
            if j == '1':
                board[i][k] = 'b'
                black_team.update({coordinated_board[i][k]: 0})
    for i in board:
        coding_board += ''.join(i)
        # print('  '.join(i))
    return coordinated_board, coding_board, white_team, black_team, loose_board


def clean_board(coord_board, white_team, black_team, un_modded_board):
    global squares, settings
    code = ''
    un_modding_board = copy. deepcopy(un_modded_board)
    for num_r, coord_r in enumerate(coord_board):
        for num_c, coord_c in enumerate(coord_r):
            if coord_c in white_team:
                un_modding_board[num_r][num_c] = 'w'
            elif coord_c in black_team:
                un_modding_board[num_r][num_c] = 'b'
    for inside in un_modding_board:
        code += ''.join(inside)
    #   print('  '.join(inside))
    # print('\n\n')
    return code
