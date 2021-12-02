def read(string):
    return open(string, "r").readlines()


if __name__ == "__main__":
    start = [0, 0, 0]
    for i in read("input.txt"):
        lis = i.replace("\n", "").split(" ")
        match lis[0]:
            case "forward":
                start[0] += int(lis[1])
                start[1] += start[2] * int(lis[1])
            case "down":
                start[2] += int(lis[1])
            case "up":
                start[2] -= int(lis[1])

    print(start[0] * start[1])


