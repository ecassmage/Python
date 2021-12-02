def getCart(size1, size2):
    lis = []
    for k in range(size1):
        for l in range(size2):
            lis.append([k, chr((l % 26) + 97)])
    return lis


if __name__ == "__main__":
    for i in range(10):
        print(f"i = {i}")
        for j in range(10):

            AtoB = getCart(i, j)
            BtoA = getCart(j, i)
            if len(AtoB) != len(BtoA):
                print(f"{len(getCart(i, j))} is a Failure since {len(getCart(j, i))}")
            print(f"\tj = {j}\t", end='')
            print(f"\t{AtoB} -> {BtoA}")
        print(f"Done i: {i}")
    pass
