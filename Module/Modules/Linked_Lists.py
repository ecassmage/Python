import random
from itertools import chain
from copy import copy


class SinglyLinked:

    object_list = []

    def __init__(self, value):
        self.value = value
        self.next = None
        self.object_list.append(self.value)

    def append_after(self, num):
        num.value = num
        num.next = self.next
        self.next = num


class DoublyLinked:

    keys = {}

    def __init__(self, value, switch=0):
        if switch == 0:
            self.prev = None
            self.value = value
            self.next = None
            self.keys.update({self.value: self})

    def key_find(self, value):
        return self.keys[value]

    def append_r(self, value):
        obj = DoublyLinked(value, 0)
        obj.next = self.next
        obj.prev = self
        self.next.prev = obj
        self.next = obj
        return obj

    def append_l(self, value):
        obj = DoublyLinked(value, 0)
        obj.next = self
        obj.prev = self.prev.next
        self.prev.next = obj
        self.prev = obj
        return obj

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        pass

    def re_add_r(self, obj):
        obj.next = self.next
        obj.prev = self
        obj.next.prev = obj
        self.next = obj
        return obj

    def re_add_l(self, obj):
        obj.next = self
        obj.prev = self.prev.next
        self.prev.next = obj
        self.prev = obj
        return obj

    def return_value(self, value):
        return self.keys[value]

    def delete(self, value):
        x = self.key_find(value)
        x.prev.next, x.next.prev = x.next, x.prev
        del self.keys[value]


class DoublyLinkedControl:
    def __init__(self):
        self.key = DoublyLinked.keys


class BetterDoubly:

    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

    def append_after(self, value):
        obj = BetterDoubly(value)
        obj.next = self.next
        obj.prev = self
        self.next.prev = obj
        self.next = obj
        return obj


def singly(list_set):
    return_list = [None] * (len(list_set))
    list_set = iter(list_set)
    first = SinglyLinked(next(list_set))
    previous = return_list[0] = first
    current = None
    for pointer, val in enumerate(list_set):
        current = return_list[pointer + 1] = SinglyLinked(val)
        previous.next = current
        previous = current
    current.next = first
    return return_list


def doubly(list_set):
    dict_set = {}
    # return_list = [None] * (len(list_set))
    first = DoublyLinked(list_set[0], 0)
    list_set[0] = first
    previous = first
    current = None
    for pointer, val in enumerate(list_set[1:]):
        current = list_set[pointer + 1] = DoublyLinked(val, 0)
        current.prev = previous
        previous.next = current
        previous = current
        # return_list[point] = SinglyLinked(val)
    first.prev = previous
    current.next = first
    return list_set


"""Unique Keys Only"""


def doubly_dict(list_set):
    dict_set = {}
    first = DoublyLinked(list_set[0], 0)
    dict_set.update({first.value: first})
    previous = first
    current = None
    for pointer, val in enumerate(list_set[1:]):
        current = DoublyLinked(val)
        dict_set.update({current.value: current})
        current.prev = previous
        previous.next = current
        previous = current
    first.prev = previous
    current.next = first
    return_dict = DoublyLinkedControl()
    return_dic = DoublyLinked(None, 1)
    print(return_dic)
    return dict_set, return_dic


def b_double(list_set):
    list_set_ = copy(list_set)
    first = list_set_[0] = BetterDoubly(list_set[0])
    previous = list_set_[0]
    current = None
    for pointer, val in enumerate(list_set_[1:]):
        list_set_[pointer].next = list_set[pointer + 1]
        current = list_set_[pointer + 1] = BetterDoubly(val)
        current.prev = list_set[pointer]
    list_set_[-1].next = list_set[0]
    first.prev = list_set[-1]
    first.next = list_set[1]
    return list_set_
