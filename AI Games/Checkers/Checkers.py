import copy
import random
from tkinter import *
import time
tk = Tk()
random.seed(a=None, version=2)
size_board = 8
size_of_squares = 100
time_delay = 1
color_1 = 'black'
color_2 = 'white'
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
all_defined_boards, all_kill_moves = {}, {}


class BoardSquare:
    def __init__(self, colour_1, colour_2, size_of_board, count_of_squares):
        color = colour_1
        color_row = colour_2
        for x in range(size_of_board):
            if color_row == colour_2:
                color = colour_1
            else:
                color = colour_2
            color_row = color
            for y in range(count_of_squares):
                x1 = x * size_of_board
                y1 = y * size_of_board
                x2 = x1 + size_of_board
                y2 = y1 + size_of_board
                canvas.create_rectangle((x1, y1, x2, y2), fill=color)
                if color == colour_1:
                    color = colour_2
                else:
                    color = colour_1


class DrawBoardPieces:
    def __init__(self, size, code_make, game_sizing):
        self.pieces = []
        x1 = size / 3
        y1 = size / 3
        x2 = size - size / 3
        y2 = size - size / 3
        for number, character in enumerate(code_make):
            # print(number % game_sizing)
            # print(character)
            if number % game_sizing == 0 and number != 0:
                x1 = size / 3
                y1 = y1 + size
                x2 = size - size / 3
                y2 = y2 + size
            elif number == 0:
                pass
            else:
                x1 = x1 + size
                x2 = x2 + size
            if character == 'w':
                self.create_piece('red', x1, y1, x2, y2)
            elif character == 'b':
                self.create_piece('blue', x1, y1, x2, y2)

    def create_piece(self, color, x1, y1, x2, y2):
        self.pieces.append(canvas.create_rectangle((x1, y1, x2, y2), fill=color))

    def del_pieces(self):
        for i in self.pieces:
            canvas.delete(i)
        self.pieces = []
        time.sleep(time_delay)


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
    [print('  '.join(i)) for i in board]
    print('\n')
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
        print('  '.join(i))
    return coordinated_board, coding_board, white_team, black_team, loose_board


def all_possibilities_explored(team, i, x, y, choice):
    team_make = []
    for x1, y1 in choice[team[i]]['move']:
        move = tuple((x + x1, y + y1))
        team_make.append(move)
        # print(move)
    return team_make


def moving_games(movement, rows, board, team, opponent, x, y, i):
    safe_moves, kill_moves = [], []
    for moves in movement:
        for row in rows:
            if abs(row) == 1:
                if moves in board[rows[row]] and abs(x - moves[0]) == 1 and abs(y - moves[1]) == 1 and \
                        moves not in team and moves not in opponent:
                    safe_moves.append(moves)
                    # break
            elif abs(row) == 2:
                if moves in board[rows[row]] and abs(x - moves[0]) == 2 and abs(y - moves[1]) == 2 and \
                        moves not in team and moves not in opponent \
                        and tuple(kill_move(team, opponent, i, moves)) in opponent:
                    # print(opponent)
                    # print('fuck you', tuple(kill_move(team, opponent, i, moves)))
                    safe_moves.append(moves)
                    kill_moves.append(moves)
                    # break
    return safe_moves, kill_moves


def all_possible_moves_that_can_be_made(board, team, opponent, color):
    team_moves, kill_moves, movement, killing_moves = {}, {}, [], []
    # print("\n%s\n%s\n%s\n%s\n" % (board, team, opponent, color))
    global white_choices, black_choices
    # white_team, black_team = {}, {}
    rows = {}
    for i in team:
        x, y = i
        tru_y = 7 - y
        if team[i] == 1:
            rows = {2: 7 - (y + 2), 1: 7 - (y + 1), -1: 7 - (y - 1), -2: 7 - (y - 2)}
        else:
            if color == 'white':
                rows = {-1: 7 - (y - 1), -2: 7 - (y - 2)}
            elif color == 'black':
                rows = {1: 7 - (y + 1), 2: 7 - (y + 2)}
        rows_temp = copy.copy(rows)
        # print('what', rows)
        for row in rows_temp:
            if (7 >= rows_temp[row] >= 0) is False:
                del rows[row]
        # print('what', rows)
        # print('true y:', tru_y)
        # exit()
        if color == 'white':
            movement = all_possibilities_explored(team, i, x, y, white_choices)
        elif color == 'black':
            movement = all_possibilities_explored(team, i, x, y, black_choices)
        safe_moves, killing_moves = moving_games(movement, rows, board, team, opponent, x, y, i)
        if len(killing_moves) > 0:
            kill_moves.update({i: killing_moves})
        if len(safe_moves) != 0:
            team_moves.update({i: safe_moves})
    return team_moves, kill_moves


def kill_move(team, opponent, piece, move):
    return int(((piece[0] - move[0]) / 2) + move[0]), int(((piece[1] - move[1]) / 2) + move[1])


def smart_move_ai(moves_to_make, attacks_to_make):
    if len(attacks_to_make) > 0:
        moves = attacks_to_make
    else:
        moves = moves_to_make
    return moves


def ai_decision_making(coordinates, code, team, opponent, color):
    global all_defined_boards, all_kill_moves
    if code not in all_defined_boards:
        moves, kill_moves = all_possible_moves_that_can_be_made(coordinates, team, opponent, color)
        all_kill_moves.update({code: kill_moves})
        all_defined_boards.update({code: moves})
    else:
        moves = all_defined_boards[code]
        if all_kill_moves[code] is True:
            kill_moves = all_kill_moves[code]
        else:
            kill_moves = {}
    moves = smart_move_ai(moves, kill_moves)
    choice_piece = list(moves)[random.randrange(0, len(moves))]
    piece_to_move = moves[choice_piece]
    move_move = piece_to_move[random.randrange(0, len(piece_to_move))]
    # print(color, list(moves), choice_piece, piece_to_move, move_move)
    team.update({move_move: team[choice_piece]})
    # print(team, opponent)
    del team[choice_piece]
    # print(team, opponent)
    # opponent.update({(6, 4): 0})
    # choice_piece = (5, 3)
    # team.update({(5, 3): 0})
    # move_move = (7, 5)
    # print(choice_piece, move_move)
    x, y = choice_piece
    # print(x, y)
    # print(opponent)
    if abs(x - move_move[0]) == 2 and abs(y - move_move[1]) == 2:
        # print(x, y)
        killed = tuple(kill_move(team, opponent, choice_piece, move_move))
        if killed in opponent:
            del opponent[killed]
        else:
            print('Something Messed UP!!!')
            exit()
    # print(opponent)
    # print(team)
    return team, opponent


def kingdom(team, color):
    global black_goal, white_goal
    for team_piece in team:
        if color == 'white':
            if team_piece in white_goal:
                team.update({team_piece: 1})
        elif color == 'black':
            if team_piece in black_goal:
                team.update({team_piece: 1})
    return team


def clean_board(coord_board, white_team, black_team, un_modded_board):
    global squares
    code = ''
    # print(coord_board)
    un_modding_board = copy. deepcopy(un_modded_board)
    for num_r, coord_r in enumerate(coord_board):
        for num_c, coord_c in enumerate(coord_r):
            if coord_c in white_team:
                un_modding_board[num_r][num_c] = 'w'
            elif coord_c in black_team:
                un_modding_board[num_r][num_c] = 'b'
    for inside in un_modding_board:
        code += ''.join(inside)
        print('  '.join(inside))
    print('\n\n')
    canvas.delete(squares.del_pieces())
    squares = DrawBoardPieces(size_of_squares, code, size_board)
    canvas.update()
    return code


def games(coordinate_board, coded_board, white_team, black_team, un_modded_board):
    for _ in range(1000):
        # White Teams Turn
        white_team, black_team = ai_decision_making(coordinate_board, coded_board, white_team, black_team, 'white')
        white_team = kingdom(white_team, 'white')
        coded_board = clean_board(coordinate_board, white_team, black_team, un_modded_board)
        # Black Teams Turn
        black_team, white_team = ai_decision_making(coordinate_board, coded_board, black_team, white_team, 'black')
        black_team = kingdom(black_team, 'black')
        coded_board = clean_board(coordinate_board, white_team, black_team, un_modded_board)
        print(_)


if __name__ == '__main__':
    canvas = Canvas(tk, width=size_of_squares*8, height=size_of_squares*8)
    canvas.pack()
    coordinate_board1, coded_board1, white_team1, black_team1, loosened_board = build_board()
    # print('ehlp', loosened_board)
    black_goal, white_goal = coordinate_board1[0], coordinate_board1[-1]
    # print(white_team1, '\n', black_team1)
    # print(white_goal, '\n', black_goal)
    # for coord in coordinate_board1:
    #     print(coord)
    # print('\n', coded_board1)
    BoardSquare(color_1, color_2, size_of_squares, size_board)
    squares = DrawBoardPieces(size_of_squares, coded_board1, size_board)
    games(coordinate_board1, coded_board1, white_team1, black_team1, loosened_board)
    tk.mainloop()
