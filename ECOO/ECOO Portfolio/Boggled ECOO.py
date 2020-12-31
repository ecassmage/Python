boggled1 = []
boggled2 = []
tick = 0
with open('E:\\ECOO\\Boggled\\DATA41.txt', 'r') as DATA41:
    DATA41.readline()
    for line in DATA41:
        tick = tick + 1
        try:
            int(line)

        except ValueError:
            pass
print(line)
