"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
This is meant to test a Double Linked list I was writing as an importable module and was testing some methods I made for
it matching its speed against a function by interacting directly with the attributes instead of intermediary methods
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
from Linked_Lists import doubly_dict


def fast(start, x, num):
    maxcup = len(x)
    print(maxcup)
    cur_cup = x[start]
    for turn in range(num):
        first = cur_cup.next
        second = first.next
        third = second.next
        musketeers = (first.value, second.value, third.value)
        cur_cup.next = third.next
        cur_cup.next.prev = cur_cup
        temp_position = maxcup if cur_cup.value == 1 else cur_cup.value - 1
        while temp_position in musketeers:
            temp_position = maxcup if temp_position == 1 else temp_position - 1
        temp_position = x[temp_position]
        first.prev = temp_position
        third.next = temp_position.next
        temp_position.next.prev = third
        temp_position.next = first
        cur_cup = cur_cup.next
    return x[1]


def game(start, x, num):
    maxcup = len(x)
    print(maxcup)
    cur_cup = x[start]
    for turn in range(num):
        first = cur_cup.next
        second = first.next
        third = second.next
        musketeers = (first.value, second.value, third.value)
        x[first.value].remove()
        x[second.value].remove()
        x[third.value].remove()
        del x[first.value]
        del x[second.value]
        del x[third.value]
        temp_position = maxcup if cur_cup.value == 1 else cur_cup.value - 1
        while temp_position in musketeers:
            temp_position = maxcup if temp_position == 1 else temp_position - 1
        x.update({first.value: first})
        x.update({second.value: second})
        x.update({third.value: third})
        x[temp_position].re_add_r(first)
        x[first.value].re_add_r(second)
        x[second.value].re_add_r(third)
        cur_cup = cur_cup.next
        if turn % 100000 == 0:
            print(turn)
    return x[1]


list_base = list(open('input.txt').readline())
# print(list_base)
for j, i in enumerate(list_base):
    list_base[j] = int(i)
# print(list_base)
for i in range(len(list_base) + 1, 1000001):
    list_base.append(i)
# print(list_base)
list_base_dict, hello = doubly_dict(list_base)
# print(hello)
# key = hello.key_find(15)
# hell = hello.delete(9)

answer = game(list_base[0], list_base_dict, 10000000)
print(answer)
print(f"The Answer to Part 2 is: {answer.next.value * answer.next.next.value}")
