input_folder = 'input.txt'
dic = dict()
count2 = 0

with open("%s" % input_folder, "r") as Day2:
    for i in Day2.readlines():
        w = i.split('-', )
        x = w[1].split(' ', 1)
        y = x[1].split(': ')
        z = y[1].strip(' ')
        t = list(z)
        count = 0
        for j in t:
            if j == y[0]:
                count = count + 1
        if int(w[0]) <= count <= int(x[0]):
            count2 = count2 + 1

print("The Answer to Part 1 is: %d" % count2)
