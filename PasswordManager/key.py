from copy import copy


def hash_key(num, hashList=None):
    if hashList is None:
        hashList = list("""abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"""
                        """-_=+,<.>/?|'";:[]}{` ~ABCDEFGHIJKLMNOPQRSTUVWXYZ""")
    for _ in range(num):
        middle = int(len(hashList) / 2)
        hashList_fh = hashList[middle:]
        hashList_lh = hashList[:middle]
        for i in reversed(range(len(hashList_fh))):
            hashList_lh.insert(i, hashList_fh[i])
        hashList = copy(hashList_lh)
    return hashList


def hash_key_short(num):
    hashList = list("""abcdefghijklmnopqrstuvwxyz12345678901234567890!@#$%^&!@#$%^&ABCDEFGHIJKLMNOPQRSTUVWXYZ""")
    for _ in range(num):
        middle = int(len(hashList) / 2)
        hashList_fh = hashList[middle:]
        hashList_lh = hashList[:middle]
        for i in reversed(range(len(hashList_fh))):
            hashList_lh.insert(i, hashList_fh[i])
        hashList = copy(hashList_lh)
    return hashList


def caesarCypher(c, lis, direction=0):
    if direction == 0:
        for _ in range(c):
            lis.insert(0, lis.pop())
        return lis
    else:
        for _ in range(c):
            lis.append(lis.pop(0))
        return lis
