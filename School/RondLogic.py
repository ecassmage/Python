from itertools import product
import copy


def cartesian(set1, set2):
    return list(product(set1, set2))


def union(set1, set2):
    SetUnion = copy.deepcopy(set1)
    for element in set2:
        if element not in SetUnion:
            SetUnion.append(element)
    return SetUnion


def intersection(set1, set2):
    SetIntersection = []
    for element in set1:
        if element in set2:
            SetIntersection.append(element)


if __name__ == "__main__":
    A = [1]
    B = [2]
    C = [3]
    D = [4]

    AXB = cartesian(A, B)
    CXD = cartesian(C, D)
    AUC = union(A, C)
    BUD = union(B, D)
    AXBUCXD = union(AXB, CXD)
    AUCXBUD = cartesian(AUC, BUD)
    print(AXBUCXD)
    print(AUCXBUD)
    Success = True
    for S in AXBUCXD:
        if S not in AUCXBUD:
            # print(f"Failure For: {S}")
            Success = False
    if Success:
        print("(A X B) U (C X D) -> (A U C) X (B U D)")
    else:
        print("(A X B) U (C X D) -/> (A U C) X (B U D)")

    # print("\n\n\n")

    Success = True
    for S in AUCXBUD:
        if S not in AXBUCXD:
            Success = False
            # print(f"Failure For: {S}")
    if Success:
        print("(A U C) X (B U D) -> (A X B) U (C X D)")
    else:
        print("(A U C) X (B U D) -/> (A X B) U (C X D)")

    pass
