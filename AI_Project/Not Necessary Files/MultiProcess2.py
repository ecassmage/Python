from multiprocessing import Pool
from time import time


class Make:
    def __init__(self, num):
        self.hi = 55
        self.num = num


def problem(x):
    j = 0
    for i in range(10000):
        j += 1
    return x


# def main():
#     if __name__ == '__main__':
#         with Pool(processes=6) as p:
#             print(p.map(problem, range(100)))


if __name__ == '__main__':
    lis = []
    for make in range(100000):
        lis.append(Make(make))
    start = time()
    with Pool(processes=2) as p:
        p.map(problem, lis)
    print(f"Multiprocessing took {time() - start}")
    start = time()
    with Pool(processes=4) as p:
        p.map(problem, lis)
    print(f"Multiprocessing took {time() - start}")
    start = time()
    with Pool(processes=6) as p:
        p.map(problem, lis)
    print(f"Multiprocessing took {time() - start}")
    start = time()
    with Pool(processes=8) as p:
        p.map(problem, lis)
    print(f"Multiprocessing took {time() - start}")
    start = time()
    for i in lis:
        problem(i)
    print(f"Not Multiprocessing took {time() - start}")
# main()
