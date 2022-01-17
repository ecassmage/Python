def hexbin(string, scale=16):
    string = string.replace("\n", "").strip()
    return str(bin(int(string, scale))[2:].zfill(len(string) * 4))


def getVerAndTyp(string, pos=0):
    return string[pos:pos+3], string[pos+3:pos+3+3], pos+3+3


def getDec(string):
    return int(string, 2)


def getOperatorVal(string, pos, code):
    return 4 if getDec(code) == 4 else 15 if string[pos] == '0' else 11


def four(string):
    number = ''
    for packet in range(0, len(string), 5):
        pkt = string[packet:packet + 5]
        number += pkt[1:]
        if pkt[0] == '0':
            return -1, packet + 5
    return -1, len(string)


def eleven(string):
    numToCount = getDec(string[1:12])
    stringOld = string
    string = string[12:]
    numberVerSum = 0
    posReturn = 0
    for _ in range(numToCount):
        Ver, Type, pos = getVerAndTyp(string)
        numberVerSum += getDec(Ver)
        print(getDec(Ver))
        r = control(string, pos, Type)
        if r[0] != -1:
            numberVerSum += r[0]
        posReturn += r[1]
        print(string[:pos+r[1]+1])
        s = string[:pos+r[1]+1]
        string = string[pos+r[1]:]
    return numberVerSum, posReturn + 1


def fifteen(string):
    numToCount = getDec(string[1:16])
    stringOld = string
    string = string[16:16+numToCount]
    numberVerSum = 0
    posReturn = 16

    while len(string) > 0:
        Ver, Type, pos = getVerAndTyp(string)
        print(getDec(Ver))
        numberVerSum += getDec(Ver)
        r = control(string, pos, Type)
        if r[0] != -1:
            numberVerSum += r[0]
        posReturn += r[1]
        string = string[pos+r[1]:]
    # print(Ver, Type, pos)
    return numberVerSum, posReturn + 1


def control(string, pos, code):
    func = {4: four, 11: eleven, 15: fifteen}
    return func[getOperatorVal(string, pos, code)](string[pos:])
    # if getDec(code) == 4:
    #     r = func[getDec(code)](string[pos:])
    #     return func[getDec(code)](string[pos:])
    # else:
    #     r = func[getOperatorVal(string, pos)](string[pos+1:])
    #
    #     return func[getOperatorVal(string, pos)](string[pos+1:])


def part1(string):
    Ver, Type, pos = getVerAndTyp(string)
    print(string)
    print(getDec(Ver))
    num = getDec(Ver)
    r = control(string, pos, Type)
    num += r[0]
    print(num)
    return num


def main(inp):
    string = ''
    for line in open(inp):
        string = hexbin(line)
    # Type, Ver, pos = getVerAndTyp(string)
    # print(Type, Ver, pos)
    # print(getDec(Type), end='   ')
    # print(getDec(Ver), end='   ')
    # print(pos)
    # print(getOperatorVal(string, pos))
    part1(string)


if __name__ == '__main__':
    main('test.txt')
    # part1('00111000000000000110111101000101001010010001001000000000')
    # part1('11101110000000001101010000001100100000100011000001100000')
