def main():
    w, x, y, z = 6, 0, 7, 15
    L1 = [-4, 10, 11, -2, 3]
    print(y and z or not (w and x))
    print((L1[2] + L1[-2]) * L1[-1] - L1[0])


def new_fn(x, n):  # Here x is a lowercase alphabetic character and n is an int

    res = (ord(x) - ord('a') + 1)*n

    return res


if __name__ == '__main__':
    main()
    print()
    print(new_fn('z', 2))
    print(type(new_fn('z', 2)))
    string = 'abcd'
    string[0] = 'b'
    print(string[0])
    pass
