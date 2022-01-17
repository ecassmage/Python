import math


def hexbin(string, scale=16):
    string = string.replace("\n", "").strip()
    return str(bin(int(string, scale))[2:].zfill(len(string) * 4))


def getVerAndTyp(string, pos=0):
    return string[pos:pos+3], string[pos+3:pos+3+3], pos+3+3


def getDec(string):
    return int(string, 2)


def getOperatorVal(string, pos, code):
    return 4 if getDec(code) == 4 else 15 if string[pos] == '0' else 11


def mul(lis):
    num = 0
    for val in lis:
        if num == 0:
            num = val
        else:
            num *= val
    return num


def hold(ver, listOfPackets):
    match ver:
        case 0:
            return [sum(listOfPackets)]
        case 1:
            return [math.prod(listOfPackets)]
            # return [mul(listOfPackets)]
        case 2:
            return [min(listOfPackets)]
        case 3:
            return [max(listOfPackets)]
        case 4:
            return listOfPackets
        case 5:
            return [1] if listOfPackets[0] > listOfPackets[1] else [0]
        case 6:
            return [1] if listOfPackets[0] < listOfPackets[1] else [0]
        case 7:
            return [1] if listOfPackets[0] == listOfPackets[1] else [0]


def four(string):
    countStr = ''
    while len(string) > 0:
        pkt = string[:5]
        string = string[5:]
        countStr += pkt[1:]
        if pkt[0] == '0':
            break
    return getDec(countStr), string


def operator(string, val=-1):
    iterations = -2 if val == -1 else 0
    VerSum = 0
    string15 = ''
    TypeP = getDec(string[3:6])
    listOfPackets = []
    while len(string) > 6 and iterations < val:
        print(string)
        Ver = getDec(string[:3])
        Type = getDec(string[3:6])
        string = string[6:]
        if len(string) > 0:
            VerSum += Ver
        else:
            break
        if Type == 4:
            output = four(string)
            listOfPackets.append(output[0])
            string = output[1]
        else:
            valImportant = string[0]
            string = string[1:]
            if valImportant == '0':
                if len(string) < 15:
                    break
                valueToSend = getDec(string[:15])
                string = string[15:]
                string15 = string[valueToSend:]
                string = string[:valueToSend]
                out = operator(string)
                VerSum += out[0]
                string = string15
                listOfPackets += hold(Type, out[2])
            else:
                if len(string) < 11:
                    break
                valueToSend = getDec(string[:11])
                string = string[11:]
                out = operator(string, valueToSend)
                VerSum += out[0]
                string = out[1]
                v = hold(Type, out[2])
                listOfPackets += v
        if val != -1:
            iterations += 1
    return VerSum, string, listOfPackets


def part1(string):
    return operator(string)


def main(inp):
    string = ''
    for line in open(inp):
        string = hexbin(line)
    print(string)
    print(part1(string))
    pass


if __name__ == '__main__':
    main('input.txt')
