import copy
import random
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
    return coordinated_board, coding_board, white_team, black_team


def all_possibilities_explored(team, i, x, y, choice):
    team_make = []
    for x1, y1 in choice[team[i]]['move']:
        move = tuple((x + x1, y + y1))
        team_make.append(move)
        # print(move)
    return team_make


def all_possible_moves_that_can_be_made(board, team, opponent, color):
    team_moves, safe_moves, movement = {}, [], []
    # print("\n%s\n%s\n%s\n%s\n" % (board, team, opponent, color))
    global white_choices, black_choices
    white_team, black_team = {}, {}
    row, row2 = [], []
    for i in team:
        x, y = i
        # print(board)
        # print(i)
        # print(x, y)
        if color == 'white':
            row = board[7 - (y - 1)]
            row2 = board[7 - (y - 2)]
            # print('kill yourself', board[7 - y])
            # print('hello', row, row2)
            movement = all_possibilities_explored(team, i, x, y, white_choices)
        elif color == 'black':
            row = board[7 - (y + 1)]
            row2 = board[7 - (y + 2)]
            # print(board[7 - y])
            # print('hellop', row, row2)
            movement = all_possibilities_explored(team, i, x, y, black_choices)

        safe_moves = []
        for moves in movement:
            # print(row, row2)
            # print(movement)
            # print('moves', moves, i)
            # print("Help me", abs(x - moves[0]), abs(y - moves[1]))
            # print(moves in row2, abs(x - moves[0]) == 2 and abs(y - moves[1]) == 2)
            # print(moves in row, abs(x - moves[0]) == 1 and abs(y - moves[1]) == 1)
            if moves in row2 and abs(x - moves[0]) == 2 and abs(y - moves[1]) == 2 and moves not in team \
                    and moves not in opponent:
                safe_moves.append(moves)
            elif moves in row and abs(x - moves[0]) == 1 and abs(y - moves[1]) == 1 and moves not in team \
                    and moves not in opponent:
                safe_moves.append(moves)
                # break
        # print(safe_moves)
        if len(safe_moves) != 0:
            team_moves.update({i: safe_moves})
    # exit()
    return team_moves


def kill_move(team, opponent, piece, move):
    return int(((piece[0] - move[0]) / 2) + move[0]), int(((piece[1] - move[1]) / 2) + move[1])


def draw_board():
    for i in range(9):
        pass


def ai_decision_making(coordinates, code, team, opponent, color):
    print(team)
    team.update({(2, 2): 0})
    global all_defined_boards
    if code not in all_defined_boards:
        moves = all_possible_moves_that_can_be_made(coordinates, team, opponent, color)
        all_defined_boards.update({code: moves})
    else:
        moves = all_defined_boards[code]
    # print(all_defined_boards)
    # print('WELP', moves)
    choice_piece = list(moves)[random.randrange(0, len(moves))]
    piece_to_move = moves[choice_piece]
    move_move = piece_to_move[random.randrange(0, len(piece_to_move))]
    print(list(moves), piece_to_move, move_move)
    # print(team, opponent)
    team.update({move_move: team[choice_piece]})
    del team[choice_piece]
    # opponent.update({(6, 4): 0})
    # choice_piece = (5, 3)
    # move_move = (7, 5)
    # print(choice_piece, move_move)
    x, y = choice_piece
    # print(x, y)
    # print(opponent)
    if abs(x - move_move[0]) == 2 and abs(y - move_move[1]) == 2:
        killed = tuple(kill_move(team, opponent, choice_piece, move_move))
        if killed in opponent:
            del opponent[killed]
        else:
            print('Something Messed UP!!!')
    # print(opponent)
    print(team)
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


def games(coordinate_board, coded_board, white_team, black_team):
    while True:
        # all_possible_moves_that_can_be_made(coordinate_board, white_team, black_team, 'white')
        ai_decision_making(coordinate_board, coded_board, white_team, black_team, 'white')
        break


if __name__ == '__main__':
    all_defined_boards = {}
    coordinate_board1, coded_board1, white_team1, black_team1 = build_board()
    black_goal, white_goal = coordinate_board1[0], coordinate_board1[-1]
    print(white_team1, '\n', black_team1)
    print(white_goal, '\n', black_goal)
    for coord in coordinate_board1:
        print(coord)
    print('\n', coded_board1)
    games(coordinate_board1, coded_board1, white_team1, black_team1)
