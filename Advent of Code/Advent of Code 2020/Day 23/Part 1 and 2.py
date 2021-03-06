from itertools import chain
cup_order_start = []


# For future self since this is new and I will probably forget
# This Cups class is built to be a doubly linked list


class Cups:
    def __init__(self, point):
        self.point = point  # self.point is meant to basically take its ().point and give back the value it is holding
        self.prev = None  # self.prev is meant to get the previous value ().prev
        self.next = None  # self.next is meant to get the next value ().next


def build_the_list(x, y):
    # print(y)
    if y == 0:
        y = None
    y = (y if y else len(x)) + 1
    cups = [None] * y
    extras = chain(x, range(len(x) + 1, y))
    first = next(extras)
    cups[first] = Cups(first)
    first = cups[first]
    prev = first
    for location in extras:
        current = cups[location] = Cups(location)
        current.prev = prev
        prev.next = current
        prev = current
        # print(cups, location)
    current.next = first
    return first, cups


def counting_cups(x, y, z1):
    z = len(y) - 1
    for irrelevant in range(0, z1):
        # print(irrelevant)
        first = x.next
        mid = first.next
        last = mid.next
        three_musketeer_cups = (first.point, mid.point, last.point)
        x.next = last.next
        x.next.prev = x
        c = 0
        # print(three_musketeer_cups)
        # cup_transfer = z if x.point == 1 else x.point - 1
        # cup_transfer = x.point
        # if cup_transfer == 1:
        #     cup_transfer = z
        # else:
        #     cup_transfer = x.point - 1
        # while True:
        #     if cup_transfer == 1:
        #         cup_transfer = z
        #     else:
        #         cup_transfer = cup_transfer - 1
        #     if cup_transfer not in three_musketeer_cups:
        #         break
        cup_transfer = z if x.point == 1 else x.point - 1
        while cup_transfer in three_musketeer_cups:
            cup_transfer = z if cup_transfer == 1 else cup_transfer - 1
        cup_transfer = y[cup_transfer]
        first.prev = cup_transfer
        last.next = cup_transfer.next
        cup_transfer.next.prev = last
        cup_transfer.next = first
        x = x.next
    return y


for line in open('E:\\Advent\\Advent of Code\\Advent of Code 2020\\Day 23\\input.txt').readlines():
    cup_order_start = tuple([int(i) for i in line])
    # print(cup_order_start)
beginning, cups_of_choice = build_the_list(cup_order_start, 0)
the_conquest = counting_cups(beginning, cups_of_choice, 100)
part_1 = ''
the_position_of_1 = the_conquest[1].next
while True:
    part_1 += str(the_position_of_1.point)
    the_position_of_1 = the_position_of_1.next
    if the_position_of_1 == the_conquest[1]:
        # print("Hello")
        break
beginning, cups_of_choice = build_the_list(cup_order_start, 1000000)
the_conquest = counting_cups(beginning, cups_of_choice, 10000000)
print("The Answer to Part 1 is: ", part_1)
print("The Answer to Part 2 is: ", the_conquest[1].next.point * the_conquest[1].next.next.point)