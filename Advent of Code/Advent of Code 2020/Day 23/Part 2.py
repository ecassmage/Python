from itertools import chain
cup_order_start = []


class Cups:
    def __init__(self, point):
        self.point = point
        self.prev = None
        self.next = None


def build_the_list(x):
    cups = [None] * (1000000 + 1)
    extras = chain(x, range(10, 1000000 + 1))
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


def counting_cups(x, y):
    z = len(y) - 1
    for irrelevant in range(0, 10000000):
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
        cup_transfer = x.point
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
beginning, cups_of_choice = build_the_list(cup_order_start)
the_conquest = counting_cups(beginning, cups_of_choice)

print("The Answer to Part 2 is: ", the_conquest[1].next.point * the_conquest[1].next.next.point)