# Start of Imports
import time
import copy
import math
from itertools import product
import random
import re
from tkinter import *
tk = Tk()
# End of Imports
# Start Program constant variables
game_size = 3  # board size
game_length = 100000  # amount of rounds that will be simulated
percent_turn_off = 95  # when program will stop notifying about time milestones
info_rep = 1000  # amount of rounds per information dump
SIZE = 90
time_delay = 2
easy = True
# End of Program constant variables
# All the pre defined variables
saved_move_sets, ai_human_move, prev_white, prev_black, we_got_it, time_elapsed, plus_minus = {}, {}, 0, 0, False, 0, 0
check_percent, percent_time = 50, []
percentages, changes, ai_saved, human_saved, mark = 0, [], {}, {}, [1, 4, 8, 12, 16, 20, 30, 50, 100]
# Last of the pre defined variables
visual_clarity = True
random.seed(a=None, version=2)
# game_length = game_length - 1


"""
    
    class Piece: builds and moves pieces around a board for which to be visibly viewable by the player all moves.
    
    class Square: class to build the board to be played upon which has changing colors
    
    possible_moves: Calculates all possible move for the current range of pieces coordinates that are defined it 
        operates only a single team at a time. It will generate all 8 moves surrounding the current piece and will 
        exclude any invalid direction that is not the move in front of it. It will also keep any move that finds an 
        opponent piece diagonally to it

    draw_board: Generates a visual board in the console as well as a code for the board based on positioning of both 
        teams pieces. This code will allow the program to recognise a previously used board cutting back on processing 
        time from having to generate another batch of coordinates as well as not override possibly optimized board moves

    checkerboard_construct: Constructs a checkerboard that will be used in the draw_board and also a coordinate board 
        which the program will be using to see all the possible positions that can hold a piece and still stay valid

    check_for_moves: Same as the possible_moves but for the human should they desire to play against the AI to better 
        see the change in intelligence and accuracy of the AI needs to be different since it is verifying that single 
        human choice is valid choice

    human_move: Rules for the human should they wish to play to guide them through picking and moving pieces validly 
        and in line with the rules

    ai_move: Rules for the AI to help it make its choice of movement. It will use random number ranges determined by how 
        many pieces and moves are currently saved in a list of generated boards

    winner: Will check if the team who made its move last has met any of the three requirements to win the round, should 
        they win, winner will send back a 1 which will then flip a switch to 'True' should black (human player) have 
        called winner. If white calls winner, the flip will remain False. At the start of each round the flip is flipped 
        to False always. if winner determines none of the 3 requirements have been met it will return a 0 meaning no one 
        has made a winning play yet.

    clean_memory: Will clean the memory of the losing team. While the game is being played all moves made by an AI will 
        be saved into a list and once clean_memory is called will take that list as well as the list holding all 
        currently generated boards and will linearly go through the generated boards and remove all movements made 
        during that losing play.

    memory_rewards: Will give a reward to the winning team. As in clean_memory memory_rewards functions the exact same 
        as clean_memory but instead of removing memory it will add the moves that won the AI the round effectively 
        increasing the chance of winning future rounds by increasing the chance the AI will randomly choose a correct 
        path of moves.

    score_sheet: Just outputs a score sheet so as to be able to easily see the change with the learning algorithm. 
        Outputs: Round    White    Black    Change_White    Change_Black    Winner    Loss/Win Ratio    Percent/5000
            Round: Rounds currently played

            White: Amount of wins for White currently

            Black: Amount of wins for Black currently

            Change_White: Amount of wins for White since last reporting

            Change_Black: Amount of wins for Black since last reporting

            Winner: Whoever won the most since last reporting possible outputs are Black, White or Tie

            Loss/Win Ratio: When reported how many times has White won more times then Black during a reporting period

            Percent/5000: Percent of wins for white in the past 5000 rounds, if less then 5000 rounds have been played 
                it will be measured out of how many total rounds have been played up to that point

    win_loop: Is used to operate the procedures used after 1 or more win conditions have been met.

    if __name__ == "__main__": This is the main loop of the program and will call the functions defined above when 
        necessary

"""


class Piece:
    def __init__(self, size, code_make, game_sizing):
        self.a = []
        x1 = size/3
        y1 = size/3
        x2 = size - size/3
        y2 = size - size/3
        for number, character in enumerate(code_make):
            # print(number % game_sizing)
            # print(character)
            if number % game_sizing == 0 and number != 0:
                x1 = size/3
                y1 = y1 + size
                x2 = size - size/3
                y2 = y2 + size
            elif number == 0:
                pass
            else:
                x1 = x1 + size
                x2 = x2 + size
            if character == 'w':
                self.create_square('red', x1, y1, x2, y2)
            elif character == 'b':
                self.create_square('blue', x1, y1, x2, y2)

    def create_square(self, color, x1, y1, x2, y2):
        self.a.append(canvas.create_rectangle((x1, y1, x2, y2), fill=color))

    def del_squares(self):
        for i in self.a:
            canvas.delete(i)
        self.a = []
        time.sleep(time_delay)


class Square:
    def __init__(self, size):
        color = 'white'
        color_row = 'black'
        for y in range(size):
            if color_row == 'black':
                color = 'white'
            else:
                color = 'black'
            color_row = color
            for x in range(size):
                x1 = x * size
                y1 = y * size
                x2 = x1 + size
                y2 = y1 + size
                canvas.create_rectangle((x1, y1, x2, y2), fill=color)
                if color == 'white':
                    color = 'black'
                else:
                    color = 'white'


def possible_moves(board, team, opponent, color):
    # opponent.append((1, 1))
    piece_moves = {}
    for individual in team:
        good_surroundings = []
        x, y = individual[0], individual[1]
        if color == 'white':
            row = board[x + 1]
        else:
            row = board[x - 1]
        # print(x, y)
        for adjacency in product(range(x-1, x+2), range(y-1, y+2)):
            if adjacency in row:
                if adjacency[1] != y and adjacency in opponent:
                    good_surroundings.append(adjacency)
                elif adjacency[1] == y and adjacency not in team and adjacency not in opponent:
                    good_surroundings.append(adjacency)
        if len(good_surroundings) == 0:
            continue
        piece_moves.update({(x, y): good_surroundings})
    #     print(team, opponent)
    #     print(good_surroundings)
    # print(piece_moves)
    return piece_moves


def draw_board(realistic_board, board, coord_white, coord_black):
    # print('coord_white', coord_white)
    # print('coord_black', coord_black)
    actual_board = copy.deepcopy(realistic_board)
    # for row_draw in actual_board:
    #     print(row_draw)
    for rows_num, rows in enumerate(board):
        for columns_num, columns in enumerate(rows):
            if (rows_num, columns_num) in coord_white:
                actual_board[rows_num][columns_num] = 'w'
            elif (rows_num, columns_num) in coord_black:
                actual_board[rows_num][columns_num] = 'b'
            else:
                actual_board[rows_num][columns_num] = str(actual_board[rows_num][columns_num])
    board_code = ''
    for row_draw in actual_board:
        # print('  '.join(row_draw))
        for column_code in row_draw:
            board_code += column_code
    # print('\n\n')
    # time.sleep(0.01)
    # print(board_code)
    return actual_board, board_code


def checkerboard_construct(x):
    row, checker_board, checker_board_coord, prev = [], [], [], 1
    for row_build in range(x):
        row, checker_board_coord_row = [], []
        for row_column in range(x):
            if prev == 1:
                row.append(0)
                checker_board_coord_row.append((row_build, row_column))
                prev = 0
            else:
                row.append(1)
                checker_board_coord_row.append((row_build, row_column))
                prev = 1
        checker_board_coord.append(checker_board_coord_row)
        checker_board.append(row)
        prev = row[0]
    return checker_board, checker_board_coord


def check_for_moves(board, team, opponent, color):
    good_surroundings = []
    x, y = team[0], team[1]
    if color == 'white':
        row = board[x + 1]
    else:
        row = board[x - 1]
    # print(x, y)
    for adjacency in product(range(x - 1, x + 2), range(y - 1, y + 2)):
        if adjacency in row:
            if adjacency[1] != y and adjacency in opponent:
                good_surroundings.append(adjacency)
            elif adjacency[1] == y and adjacency not in team and adjacency not in opponent:
                good_surroundings.append(adjacency)
    return good_surroundings


def human_move(visual_board, computer_board, human_team, opponent_team):
    while True:
        print('Currently in play pieces for human: ', human_team)
        print('Currently in play pieces for AI: ', opponent_team)
        piece = input("which piece would you like to move?(1, 1): ")
        piece = re.findall(r'\d{1,%d}' % game_size, piece)
        for num, word in enumerate(piece):
            piece[num] = int(word)
        piece = tuple(piece)
        print(repr(piece))
        if piece in human_team:
            break
    while True:
        moves = check_for_moves(computer_board, piece, opponent_team, 'black')
        print('Current moves that can be made: ', moves)
        print('Currently in play pieces for AI: ', opponent_team)
        move = input("Where would you like to move to?: ")
        move = re.findall(r'\d{1,%d}' % game_size, move)
        for num, word in enumerate(move):
            move[num] = int(word)
        move = tuple(move)
        print(repr(piece))
        if move in moves:
            break
    human_team.pop(human_team.index(piece))
    human_team.append(move)
    if move in opponent_team:
        opponent_team.pop(opponent_team.index(move))
    return human_team, opponent_team


def ai_move(real_moves, game_board, team, opponent):
    keys = list(real_moves)
    reap = random.randrange(0, len(real_moves))
    choice_piece = keys[reap]
    choice = real_moves[keys[reap]]
    reap = random.randrange(0, len(choice))
    choice_move = choice[reap]
    team.pop(team.index(choice_piece))
    team.append(choice_move)
    if choice_move in opponent:
        opponent.pop(opponent.index(choice_move))
    return team, opponent, choice_piece, choice_move


def winner(team, team_goal, opponent_team, moves):
    for piece in team:
        if piece in team_goal:
            return 1
    if len(moves) == 0 or len(opponent_team) == 0:
        return 1
    return 0


def clean_memory(loser_memory, moves_made):
    for human_code in moves_made:
        one, two = False, False
        memory_1 = loser_memory[human_code]
        # print('mem', memory_1)
        human_modification = loser_memory[human_code][moves_made[human_code][0]]
        length = len(loser_memory[human_code])
        # print('human modification', human_modification, length)
        for num, removing_bad in enumerate(human_modification):
            if removing_bad == moves_made[human_code][1]:
                if len(memory_1) == 1:
                    one = True
                if len(human_modification) == 1:
                    two = True
                if one and two:
                    del loser_memory[human_code]
                elif two:
                    del memory_1[moves_made[human_code][0]]
                else:
                    human_modification.pop(num)
                break
    return loser_memory


def memory_rewards(winner_mem_storage, winning_play):
    # print(winning_play)
    # print(winner_mem_storage)
    for human_code in winning_play:
        memory_1 = winner_mem_storage[human_code]
        # print('mem', memory_1)
        # print('mem', memory_1)
        human_modification = winner_mem_storage[human_code][winning_play[human_code][0]]
        length = len(winner_mem_storage[human_code])
        # print('human modification', human_modification, length)
        human_modification.append(winning_play[human_code][1])
    # print(winner_mem_storage)
    return winner_mem_storage


def score_sheet(round_num, w, prev_w, b, prev_b, rounded):
    global we_got_it, time_elapsed, plus_minus, percentages, changes, check_percent, percent_turn_off
    white_wins = 0
    print(round_num, end='')
    if w != 0:
        for i in range(0, 14 - int(math.log10(round_num))):
            print(' ', end='')
    else:
        print('              ', end='')
    print(white, end='')
    pw, pb = (w - prev_w), (b - prev_b)
    if w != 0:
        for i in range(0, 14 - int(math.log10(w))):
            print(' ', end='')
    else:
        print('              ', end='')
    print(b, end='')
    if b != 0:
        for i in range(0, 13 - int(math.log10(b))):
            print(' ', end='')
    else:
        print('             ', end='')
    print(pw, end='')
    if pw != 0:
        for i in range(0, 14 - int(math.log10(pw))):
            print(' ', end='')
    else:
        print('              ', end='')
    print(pb, end='')
    if pb != 0:
        for i in range(0, 14 - int(math.log10(pb))):
            print(' ', end='')
    else:
        print('              ', end='')
    if pw > pb:
        print('White', end='')
        plus_minus += 1
    elif pb > pw:
        print('Black', end='')
        plus_minus -= 1
    else:
        print('Tie  ', end='')
    if plus_minus != 0:
        for i in range(0, 10 - int(math.log10(abs(plus_minus)))):
            print(' ', end='')
    else:
        print('          ', end='')
    if plus_minus >= 0:
        print('+%d' % plus_minus, end='')
    else:
        print('%d' % plus_minus, end='')
    changes.append(pw)
    if len(changes) > 5:
        changes.pop(0)
    if rounded <= 5000 and visual_clarity is False:
        percentages = (w / rounded) * 100
    elif visual_clarity is False:
        for i in changes:
            white_wins += i
        percentages = (white_wins / 5000) * 100
    elif visual_clarity:
        percentages = (w / rounded) * 100
    print('          ', end='')
    print(format(percentages, '.2f'), end='%\n')
    if we_got_it is False and rounded > 1000 and percentages >= check_percent:
        for _ in range(10):
            if percentages >= check_percent:
                time_elapsed = time.process_time()
                print('It took', format(time_elapsed, '.2f'), 'to achieve this %d%% accuracy' % check_percent)
                percent_time.append(time_elapsed)
                check_percent += 5
                if percentages >= percent_turn_off:
                    we_got_it = True
            else:
                break
    # if percentages >= 85 and rounded > 1000 and eighty_five is False:
    #     eighty_five_num = time.process_time()
    #     print('It took ', format(eighty_five_num, '.2f'), 'to achieve this 85% accuracy')
    #     eighty_five = True
    # if percentages >= 90 and rounded > 1000 and ninety is False:
    #     ninety_num = time.process_time()
    #     print('It took ', format(ninety_num, '.2f'), 'to achieve this 90% accuracy')
    #     ninety = True
    # if percentages >= 95 and rounded > 1000 and ninety_five is False:
    #     ninety_five_num = time.process_time()
    #     print('It took ', format(ninety_five_num, '.2f'), 'to achieve this 95% accuracy')
    #     ninety_five = True


# def win_loop(lose_move_sets, lose_ai_moves, win_move_sets, win_ai_moves, team, difficulty, team_dif):
#     team += 1
#     lose_move_sets = clean_memory(lose_move_sets, lose_ai_moves)
#     if difficulty is False or team_dif == 'white':
#         win_move_sets = memory_rewards(win_move_sets, win_ai_moves)
#     return lose_move_sets, win_move_sets, team


black, white, winning = 0, 0, []
if __name__ == "__main__":
    if visual_clarity:
        canvas = Canvas(tk, height=SIZE * game_size, width=SIZE * game_size)
        canvas.pack()
        Square(SIZE)
    # canvas.update()
    automatic = 'no'
    while True:
        automatic = input("Do you want to play?: ")
        if automatic == 'yes':
            automatic = 0
            break
        elif automatic == 'no':
            automatic = 1
            break
    c = 0
    print('Round          White          Black    :    Change_White   Change_Black')
    time.process_time()
    if visual_clarity:
        checkerboard, checkerboard_coord = checkerboard_construct(game_size)
        team_white = copy.copy(checkerboard_coord[0])
        team_black = copy.copy(checkerboard_coord[-1])
        current_set, code = draw_board(checkerboard, checkerboard_coord, team_white, team_black)
        squares = Piece(SIZE, code, game_size)
    while True:
        c += 1
        checkerboard, checkerboard_coord = checkerboard_construct(game_size)
        team_white = copy.copy(checkerboard_coord[0])
        team_black = copy.copy(checkerboard_coord[-1])
        team_white_goal = copy.copy(team_black)
        team_black_goal = copy.copy(team_white)
        current_set, code = draw_board(checkerboard, checkerboard_coord, team_white, team_black)
        if visual_clarity:
            canvas.delete(squares.del_squares())
            squares = Piece(SIZE, code, game_size)
            canvas.update()
        try:
            while True:
                if automatic == 0:
                    team_black, team_white = human_move(current_set, checkerboard_coord, team_black, team_white)
                    current_set, code = draw_board(checkerboard, checkerboard_coord, team_white, team_black)
                    if visual_clarity:
                        canvas.delete(squares.del_squares())
                        squares = Piece(SIZE, code, game_size)
                        canvas.update()
                else:
                    if code not in ai_human_move:
                        realized_moves = possible_moves(checkerboard_coord, team_black, team_white, 'black')
                        ai_human_move.update({code: realized_moves})
                    realized_moves = ai_human_move[code]
                    answer = winner(team_white, team_white_goal, team_black, realized_moves)
                    if answer == 1:
                        win = False
                        break
                    team_black, team_white, piece_chosen, move_chosen = ai_move(
                        realized_moves, checkerboard_coord, team_black, team_white)
                    human_saved.update({code: (piece_chosen, move_chosen)})
                    current_set, code = draw_board(checkerboard, checkerboard_coord, team_white, team_black)
                    if visual_clarity:
                        canvas.delete(squares.del_squares())
                        squares = Piece(SIZE, code, game_size)
                        canvas.update()
                if code not in saved_move_sets:
                    realized_moves = possible_moves(checkerboard_coord, team_white, team_black, 'white')
                    saved_move_sets.update({code: realized_moves})
                realized_moves = saved_move_sets[code]
                answer = winner(team_black, team_black_goal, team_white, realized_moves)
                if answer == 1:
                    win = True
                    break
                team_white, team_black, piece_chosen, move_chosen = ai_move(
                    realized_moves, checkerboard_coord, team_white, team_black)
                ai_saved.update({code: (piece_chosen, move_chosen)})
                current_set, code = draw_board(checkerboard, checkerboard_coord, team_white, team_black)
                if visual_clarity:
                    canvas.delete(squares.del_squares())
                    squares = Piece(SIZE, code, game_size)
                    canvas.update()
            if visual_clarity:
                time.sleep(1)
            if win:
                black += 1
                # saved_move_sets, ai_human_move, black = win_loop(
                #     saved_move_sets, ai_saved, ai_human_move, human_saved, black, easy, 'black')
                saved_move_sets = clean_memory(saved_move_sets, ai_saved)
                # ai_human_move = memory_rewards(ai_human_move, human_saved)
                winning.append('black')
            else:
                # ai_human_move, saved_move_sets, white = win_loop(
                #     ai_human_move, human_saved, saved_move_sets, ai_saved, white, easy, 'white')
                white += 1
                # ai_human_move = clean_memory(ai_human_move, human_saved)
                saved_move_sets = memory_rewards(saved_move_sets, ai_saved)
                winning.append('white')
            human_saved, ai_saved = {}, {}
            if c in mark or c % info_rep == 0 and visual_clarity is False:
                score_sheet(c, white, prev_white, black, prev_black, c)
                prev_white, prev_black = white, black
            elif visual_clarity:
                score_sheet(c, white, prev_white, black, prev_black, c)
                prev_white, prev_black = white, black
            if c >= game_length:
                break
        except MemoryError:
            print("Program hit a problem with memory size so a crash has occurred")
            score_sheet(c, white, prev_white, black, prev_black, c)
            prev_white, prev_black = white, black
            break
    tk.mainloop()
print("White Scores: ", white, '\nBlack Scores: ', black)
# print(winning)
for i, j in enumerate(percent_time):
    print('It took ', format(j, '.2f'), 'to achieve this %d%% accuracy' % (50 + i * 5))
difference = white - black
if difference == 0:
    print('white and black won the same amount of games.')
elif difference > 0:
    print('white won %d more games then black' % difference)
else:
    print('white won %d less games then black' % abs(difference))
