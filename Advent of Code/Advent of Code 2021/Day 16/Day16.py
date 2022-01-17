def readHex(string, LITERAL=False):
    ptr = 0
    version = ''
    typeID = ''
    sumNum = 0
    while ptr < len(string):
        if version == '':
            version = string[ptr:ptr+3]
            sumNum += int(version, 2)
            print(int(version, 2))
            ptr += 3

        elif typeID == '':
            typeID = string[ptr:ptr + 3]
            ptr += 3

        elif typeID != '100':
            bitRep = 11 if string[ptr] == '1' else 15
            ptr += 1
            num = int(string[ptr:ptr+bitRep], 2)
            ptr += bitRep
            return sumNum + readHex(string[ptr:ptr+num])
        else:
            num = ''
            while True:
                packet = string[ptr:ptr+5]
                num += packet[1:5]
                ptr += 5
                if packet[0] == '0':
                    break
            version = ''
            typeID = ''

    return sumNum


def hexbin(string, scale=16):
    return str(bin(int(string, scale))[2:].zfill(len(string) * 4))


def main(string):
    hexadecimal = ""
    for line in open(string):
        hexadecimal += line.strip()
    strng = hexbin(hexadecimal)
    print(strng)
    print(readHex(strng))
    pass


if __name__ == '__main__':
    main('test.txt')
    pass
