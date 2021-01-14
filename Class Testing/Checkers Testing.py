from tkinter import Tk, Canvas
import time
import random
random.seed(a=None, version=2)
tk = Tk()
global canvas


class Piece:

    full_piece_list = []

    def __init__(self, x_coord, y_coord, color, size, adjacency):
        self.x_coord, self.y_coord, self.color, self.rank = x_coord, y_coord, color, 'Pawn'
        self.size = size
        self.adjacent = adjacency
        if color != 'Empty' and color != 'ODD' and color != 'EVEN':
            self.full_piece_list.append(self.full_coord)
            self.rectangle = []
            # self.place = self.moved_piece(size)
            size_x, size_y = size / 3, size / 3
            self.rectangle = [(self.x_coord * size) + size_x, (self.y_coord * size) + size_y,
                              (self.x_coord * size) + size - size_x, (self.y_coord * size) + size - size_y]
            self.place = self.create_piece()

    @property
    def full_coord(self):
        return tuple((self.x_coord, self.y_coord))

    @full_coord.setter
    def full_coord(self, new_coord):
        print('This is it', self.full_piece_list)
        self.x_coord = new_coord[0]
        self.y_coord = new_coord[1]
        canvas.delete(self.place)
        self.place = self.moved_piece(self.size)
        canvas.update()
        pass

    def king(self):
        return [
            (self.x_coord - 1, self.y_coord - 1), (self.x_coord + 1, self.y_coord - 1),
            (self.x_coord - 1, self.y_coord + 1), (self.x_coord + 1, self.y_coord + 1)]

    def create_piece(self):
        return canvas.create_rectangle((self.rectangle[0], self.rectangle[1],
                                        self.rectangle[2], self.rectangle[3]),
                                       fill=self.color)

    def moved_piece(self, size):
        size_x, size_y = size / 3, size / 3
        self.rectangle = [(self.x_coord * size) + size_x, (self.y_coord * size) + size_y,
                          (self.x_coord * size) + size - size_x, (self.y_coord * size) + size - size_y]
        return self.create_piece()

    def ai_choice(self):
        self.adjacent = 'hello'
        return


class Black(Piece):

    piece_list = []

    def __init__(self, x_coord, y_coord, color, size):
        super().__init__(x_coord, y_coord, color, size, self.pawn(x_coord, y_coord))
        self.piece_list.append(self.full_coord)

    @staticmethod
    def pawn(x_coord, y_coord):
        return [(x_coord - 1, y_coord - 1), (x_coord + 1, y_coord - 1)]

    def fetch_adjacent(self):
        temp = []
        print(self.adjacent)
        for j, i in enumerate(reversed(self.adjacent)):
            if i in White.piece_list:
                coord_temp = tuple((self.x_coord + 2 * (i[0] - self.x_coord), self.y_coord + 2 * (i[1] - self.y_coord)))
                if coord_temp not in self.full_piece_list:
                    temp.append(coord_temp)
            self.adjacent = temp
        print(self.adjacent)
        return self.adjacent

    def kill_piece(self, coordinate):
        self.piece_list.pop(self.piece_list.index(coordinate))
        self.full_piece_list.pop(self.full_piece_list.index(coordinate))


class White(Piece):

    piece_list = []

    def __init__(self, x_coord, y_coord, color, size):
        super().__init__(x_coord, y_coord, color, size, self.pawn(x_coord, y_coord))
        # self.adjacent = self.pawn()
        self.piece_list.append(self.full_coord)

    @staticmethod
    def pawn(x_coord, y_coord):
        return [(x_coord - 1, y_coord + 1), (x_coord + 1, y_coord + 1)]

    def fetch_adjacent(self):
        temp = []
        print(self.adjacent)
        for j, i in enumerate(reversed(self.adjacent)):
            if i in Black.piece_list:
                coord_temp = tuple((self.x_coord + 2 * (i[0] - self.x_coord), self.y_coord + 2 * (i[1] - self.y_coord)))
                if coord_temp not in self.full_piece_list:
                    temp.append(coord_temp)
            self.adjacent = temp
        print(self.adjacent)
        return self.adjacent

    def kill_piece(self, coordinate):
        self.piece_list.pop(self.piece_list.index(coordinate))
        self.full_piece_list.pop(self.full_piece_list.index(coordinate))


class Empty(Piece):
    def __init__(self, x_coord, y_coord, color, size):
        super().__init__(x_coord, y_coord, color, size, [
            (x_coord - 1, y_coord - 1),
            (x_coord + 1, y_coord - 1),
            (x_coord - 1, y_coord + 1),
            (x_coord + 1, y_coord + 1)
        ])


class Board:
    def __init__(self, square_count, squares_size, color_1, color_2):
        global canvas
        canvas = Canvas(tk, width=square_count*squares_size, height=square_count*squares_size)
        canvas.pack()
        for y in range(square_count):
            y1 = y * square_size
            y2 = y1 + square_size
            for x in range(square_count):
                x1 = x * square_size
                x2 = x1 + square_size
                if (x+y) % 2 == 0:
                    color = color_1
                else:
                    color = color_2
                canvas.create_rectangle((x1, y1, x2, y2), fill=color)


def object_piece_create(size):
    wo, bo, eo, a = [], [], [], []
    for y in range(size):
        for x in range(size):
            if (x + y) % 2 == 0:
                if y < 3:
                    wo.append(White(x, y, 'Red', square_size))
                elif y >= (size - 3):
                    bo.append(Black(x, y, 'Blue', square_size))
                a.append(Piece(x, y, 'ODD', square_size, None))
            else:
                # eo.append(Empty(x, y, 'Empty', square_size))
                a.append(Piece(x, y, 'EVEN', square_size, None))
    return wo, bo, eo, a


def ai_chose(team_objects, opponent_objects, total_objects):
    while True:
        chosen_object = random.randrange(0, len(team_objects))
        chosen_object = 1
        adjacent_list = team_objects[chosen_object].fetch_adjacent()
        print(adjacent_list)
        break
    return


def random_things():
    for num, i in enumerate(all_objects):
        if num % 8 == 0:
            print('\n')
        print(i.color, end='  ')
    print('\n')
    black_objects[4].full_coord = (3, 3)
    print(black_objects[4].full_coord)
    print(black_objects)
    print(black_objects[2].full_coord)
    print(black_objects[2].adjacent)
    print(white_objects[2].full_coord)
    print(white_objects[2].adjacent)
    print('White', White.piece_list)
    print('Black', Black.piece_list)
    print('Black', Black.full_piece_list)
    print('White', White.full_piece_list)
    print('Full', Piece.full_piece_list)
    # black_objects.append(Black(3, 3, 'Black', square_size))
    # black_objects[4].full_coord = tuple((4, 4))
    print(black_objects[-1].adjacent)
    print(black_objects[-1].fetch_adjacent())
    print(black_objects[-1].adjacent)


game_size, square_size = 8, 150
if __name__ == '__main__':
    Board(game_size, square_size, 'Black', 'White')
    white_objects, black_objects, empty_objects, all_objects = object_piece_create(game_size)
    canvas.update()
    random_things()
    ai_chose(white_objects, black_objects, all_objects)
    # black_objects[3].moved_piece()
    tk.mainloop()
# print(a[5].x_coord, a[5].y_coord)
# print(a[5].full_coord())

