import copy
import random
from tkinter import *
import time
import re
global black_goal, white_goal
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
all_defined_boards, all_kill_moves, winner = {}, {}, []
global settings


class Check:

    def __init__(self, value):
        self.dig = value
        self.isfloat = self.float_check(value)
        self.make_bool = self.making_bool(value)

    @staticmethod
    def float_check(value):
        try:
            if float(value) and value.find('.') == 1:
                return True
        except ValueError:
            return False

    @staticmethod
    def making_bool(value):
        if value == 'True':
            return True
        else:
            return False


# def isfloat(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False


class BoardSquare:
    def __init__(self, colour_1, colour_2, size_of_board, count_of_squares):
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
        global settings
        self.pieces = []
        x1 = size / 3
        y1 = size / 3
        x2 = size - size / 3
        y2 = size - size / 3
        for number, character in enumerate(code_make):
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
                self.create_piece(settings['color'][2], x1, y1, x2, y2)
            elif character == 'b':
                self.create_piece(settings['color'][3], x1, y1, x2, y2)

    def create_piece(self, color, x1, y1, x2, y2):
        self.pieces.append(canvas.create_rectangle((x1, y1, x2, y2), fill=color))

    def del_pieces(self):
        for i in self.pieces:
            canvas.delete(i)
        self.pieces = []
        time.sleep(settings['td'][0])


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


def all_possibilities_explored(team, i, x, y, choice):
    team_make = []
    for x1, y1 in choice[team[i]]['move']:
        move = tuple((x + x1, y + y1))
        team_make.append(move)
    return team_make


def moving_games(movement, rows, board, team, opponent, x, y, i):
    safe_moves, kill_moves = [], []
    for moves in movement:
        for row in rows:
            if abs(row) == 1:
                if moves in board[rows[row]] and abs(x - moves[0]) == 1 and abs(y - moves[1]) == 1 and \
                        moves not in team and moves not in opponent:
                    safe_moves.append(moves)
            elif abs(row) == 2:
                if moves in board[rows[row]] and abs(x - moves[0]) == 2 and abs(y - moves[1]) == 2 and \
                        moves not in team and moves not in opponent \
                        and tuple(kill_move(i, moves)) in opponent:
                    safe_moves.append(moves)
                    kill_moves.append(moves)
    return safe_moves, kill_moves


def all_possible_moves_that_can_be_made(board, team, opponent, color):
    team_moves, kill_moves, movement, killing_moves = {}, {}, [], []
    global white_choices, black_choices
    rows = {}
    for i in team:
        x, y = i
        if team[i] == 1:
            rows = {2: 7 - (y + 2), 1: 7 - (y + 1), -1: 7 - (y - 1), -2: 7 - (y - 2)}
        else:
            if color == 'white':
                rows = {-1: 7 - (y - 1), -2: 7 - (y - 2)}
            elif color == 'black':
                rows = {1: 7 - (y + 1), 2: 7 - (y + 2)}
        rows_temp = copy.copy(rows)
        for row in rows_temp:
            if (7 >= rows_temp[row] >= 0) is False:
                del rows[row]
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


def kill_move(piece, move):
    return int(((piece[0] - move[0]) / 2) + move[0]), int(((piece[1] - move[1]) / 2) + move[1])


def advanced_check(moves_to_make, opponent, color, board_coord):
    temp_move_pieces = {}
    for moves_of_piece in moves_to_make:
        temp_moves = []
        if color == 'white':
            if moves_of_piece in white_goal:
                continue
        elif color == 'black':
            if moves_of_piece in black_goal:
                continue
        for individual in moves_to_make[moves_of_piece]:
            adjacency = [(individual[0] - 1, individual[1] + 1), (individual[0] + 1, individual[1] + 1),
                         (individual[0] - 1, individual[1] - 1), (individual[0] + 1, individual[1] - 1)]
            diagonals = {0: 3, 1: 2, 2: 3, 3: 0}
            for adjacency_xy in adjacency:

                if adjacency_xy in opponent:
                    adjacency_caught = adjacency.index(adjacency_xy)
                    opposite_adjacency = diagonals[adjacency_caught]
                    # print(repr(adjacency_caught), repr(opposite_adjacency))
                    if opponent[adjacency_xy] == 0:
                        if (color == 'white') and \
                                (adjacency_caught == 2 or adjacency_caught == 3) and \
                                (adjacency[opposite_adjacency] in
                                 board_coord[7 - adjacency[opposite_adjacency][1]]):
                            # print('hello')
                            break
                        elif (color == 'black') and \
                                (adjacency_caught == 0 or adjacency_caught == 1) and \
                                (adjacency[opposite_adjacency] in
                                 board_coord[7 - adjacency[opposite_adjacency][1]]):
                            break
                    elif (opponent[adjacency_xy] == 1) and \
                            (adjacency[opposite_adjacency] in board_coord[7 - adjacency[opposite_adjacency][1]]):
                        continue
            else:
                temp_moves.append(individual)
        if len(temp_moves) > 0:
            temp_move_pieces.update({moves_of_piece: temp_moves})
    return temp_move_pieces


def smart_move_ai(moves_to_make, attacks_to_make, opponent, color, board_coord):
    if len(attacks_to_make) > 0:
        moves = attacks_to_make
    else:
        moves = moves_to_make
        temp_move_pieces = advanced_check(moves_to_make, opponent, color, board_coord)
        if len(temp_move_pieces) > 0:
            moves = temp_move_pieces
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
    # moves, kill_moves = all_possible_moves_that_can_be_made(coordinates, team, opponent, color)
    # all_kill_moves.update({code: kill_moves})
    # all_defined_boards.update({code: moves})
    if color == 'white':
        moves = smart_move_ai(moves, kill_moves, opponent, color, coordinates)
    # moves = smart_move_ai(moves, kill_moves, team, opponent, color)
    print(moves)
    if len(moves) < 2:
        print(moves)
        pass
    choice_piece = list(moves)[random.randrange(0, len(moves))]
    piece_to_move = moves[choice_piece]
    move_move = piece_to_move[random.randrange(0, len(piece_to_move))]
    team.update({move_move: team[choice_piece]})
    del team[choice_piece]
    x, y = choice_piece
    if abs(x - move_move[0]) == 2 and abs(y - move_move[1]) == 2:
        killed = tuple(kill_move(choice_piece, move_move))
        if killed in opponent:
            del opponent[killed]
        else:
            print('Something Messed UP!!!')
            exit()
    return team, opponent


def kingdom(team, color):
    for team_piece in team:
        if color == 'white':
            if team_piece in white_goal:
                team.update({team_piece: 1})
        elif color == 'black':
            if team_piece in black_goal:
                team.update({team_piece: 1})
    return team


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
    #     print('  '.join(inside))
    # print('\n\n')
    if settings['automatic'][0]:
        canvas.delete(squares.del_pieces())
        squares = DrawBoardPieces(settings['sos'][0], code, settings['sb'][0])
        canvas.update()
    return code


def games(coordinate_board, coded_board, white_team, black_team, un_modded_board):
    global prev
    just_played = 'white'
    while True:
        try:
            # White Teams Turn
            white_team, black_team = ai_decision_making(coordinate_board, coded_board, white_team, black_team, 'white')
            white_team = kingdom(white_team, 'white')
            coded_board = clean_board(coordinate_board, white_team, black_team, un_modded_board)
            just_played = 'white'
            # Black Teams Turn
            black_team, white_team = ai_decision_making(coordinate_board, coded_board, black_team, white_team, 'black')
            black_team = kingdom(black_team, 'black')
            coded_board = clean_board(coordinate_board, white_team, black_team, un_modded_board)
            just_played = 'black'
        except ValueError:
            print("A winner has won")
            winner.append(just_played)
            print((time.process_time() - prev))
            prev = time.process_time()
            return


def pre_game_setup():
    global canvas, prev, settings, squares
    setting_encoded, settings, squares = open('Checkers input\\Checkers_Input.txt', 'r'), {}, []
    for i in setting_encoded:
        if i[0] == '#' or i[0] == '\n':
            if i[0] == '#':
                print(i)
            continue
        line, setting_num = re.findall(r"[a-zA-Z0-9._]+", i), []
        setting_name = line[0]
        for j in range(1, len(line), 2):
            current = Check(line[j]).make_bool
            if Check(line[j]).isfloat:
                setting_num.append(float(line[j]))
            elif line[j].isdigit():
                setting_num.append(int(line[j]))
            elif current:
                print(current)
                print('hello')
                setting_num.append(current)
            else:
                setting_num.append(line[j])
        settings.update({setting_name: setting_num})
    setting_encoded.close()
    print(repr(settings))
    # if settings['automatic'][0] == 0:
    #     settings.update({'automatic': [False]})
    # elif settings['automatic'][0] == 1:
    #     settings.update({'automatic': [True]})
    canvas = Canvas(tk, width=settings['sos'][0] * 8, height=settings['sos'][0] * 8)
    if settings['automatic'][0]:
        canvas.pack()
        BoardSquare(settings['color'][0], settings['color'][1], settings['sos'][0], settings['sb'][0])
    prev = time.process_time()
    return canvas, prev, settings, squares


def end_game_write():
    white_wins, black_wins = 0, 0
    for i in winner:
        if i == 'white':
            white_wins += 1
        elif i == 'black':
            black_wins += 1
    print('%s won %d times\n%s won %d times.' % (settings['color'][2], white_wins, settings['color'][3], black_wins))
    if settings['automatic'][0]:
        tk.destroy()
        tk.mainloop()


def round_control():
    global canvas, prev, settings, squares, black_goal, white_goal
    for games_history in range(settings['game_length'][0]):
        coordinate_board, coded_board1, white_team1, black_team1, loosened_board = build_board()
        black_goal, white_goal = coordinate_board[0], coordinate_board[-1]
        if settings['automatic'][0] is True:
            if games_history > 0:
                canvas.delete(squares.del_pieces())
            squares = DrawBoardPieces(settings['sos'][0], coded_board1, settings['sb'][0])
            canvas.update()
        games(coordinate_board, coded_board1, white_team1, black_team1, loosened_board)


# if __name__ == '__main__':
canvas, prev, settings, squares = pre_game_setup()
round_control()
end_game_write()
