from itertools import combinations, tee
from multiprocessing import Pool
from os import cpu_count
import time


def generator(o, p):
    temp_gen = combinations(o, p)
    for i in temp_gen:
        yield i


def multiFunction(tup_1):
    list_1, num_1 = tup_1
    list_length = 0
    generated_combination = generator(list_1, num_1)
    for _ in generated_combination:
        list_length += 1
    print(f"assert(choose({len(list_1)}, {num_1}) == {list_length});\n", end='')


""" 
No Multiprocessing: 39.12065291404724s with Pypy
With Multiprocessing: 14.713973999023438s with Pypy
No Multiprocessing: 130.5861542224884s No Pypy
With Multiprocessing: 46.00603222846985s No Pypy
"""


if __name__ == '__main__':
    start = time.time()
    all_combos = []
    max_n = 30
    for n in range(max_n):
        lis = [i for i in range(n)]
        for m in range(n + 1):
            all_combos.append(tuple((lis, m)))
            # generated_combination = generator(lis, m)
    list_of_combos = []
    # for combo in all_combos:
    #     multiFunction(combo)
    with Pool(processes=cpu_count() - 1) as p:
        p.map(multiFunction, all_combos)
    print(len(all_combos))
    print(f"The time is {time.time() - start}")
