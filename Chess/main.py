def computerBoard():
    board = []
    for y in range(8):
        row = []
        for x in range(8):
            row.append((x, y))
        board.append(row)
    for y in board:
        print(y)
    return


def main():
    computerBoard()
    return


if __name__ == "__main__":
    main()
