def CollectInfo(ID: list, window):
    coord = window.window.coords(ID[0])
    IDInfo = {'size': coord[3]-coord[1], 'coord': coord, 'id': ID}
    return IDInfo


def sort(listO):
    listO.sort(reverse=True, key=lambda x: x['size'])


def CollisionCoord(coord1, coord2):
    return (coord1[1] <= coord2[1] < coord1[3] or coord1[1] < coord2[3] <= coord1[3]) or (coord2[1] <= coord1[1] < coord2[3] or coord2[1] < coord1[3] <= coord2[3])


def FindFitNext(listO):
    sort(listO)
    listInOrder = []

    for element in listO:
        for pos in listInOrder:
            for elementPos in pos:
                if CollisionCoord(element['coord'], elementPos['coord']):
                    break
            else:
                for i in reversed(range(len(pos))):
                    if element['coord'][1] <= dict(pos[i])['coord'][3]:
                        pos.insert(i, element)
                        break
                else:
                    pos.append(element)
                break
        else:
            listInOrder.append([element])
    return listInOrder


if __name__ == "__main__":
    INFOLIST = [
        {'size': 80-20, 'coord': [0, 25, 100, 75], 'id': [1]},
        {'size': 60-40, 'coord': [0, 40, 100, 60], 'id': [2]},
        {'size': 50-20, 'coord': [0, 20, 100, 50], 'id': [3]},
        {'size': 80-50, 'coord': [0, 50, 100, 80], 'id': [4]},
        {'size': 40-20, 'coord': [0, 20, 100, 40], 'id': [5]},
        {'size': 100-0, 'coord': [0, 0, 100, 100], 'id': [6]},
        {'size': 90-80, 'coord': [0, 80, 100, 90], 'id': [7]},
    ]
    sort(INFOLIST)
    print(INFOLIST)
    print()
    temp = FindFitNext(INFOLIST)
    for elementIn in temp:
        print(elementIn)
    # Total Size Columns is 4
    #
    pass
