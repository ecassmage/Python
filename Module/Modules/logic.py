def xor(truth_val_1, truth_val_2):
    print()
    if (truth_val_1 or truth_val_2) and truth_val_1 != truth_val_2:
        return True
    else:
        return False


def nand(truth_val_1, truth_val_2):
    if not (truth_val_1 and truth_val_2):
        return True
    else:
        return False


def nor(truth_val_1, truth_val_2):
    if not (truth_val_1 or truth_val_2):
        return True
    else:
        return False


def xnor(truth_val_1, truth_val_2):
    if truth_val_1 == truth_val_2:
        return True
    else:
        return False
