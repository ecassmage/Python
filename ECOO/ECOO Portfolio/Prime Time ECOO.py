import math

coded = []
library = dict()
alphabet = {'00': ' ', '01': 'A', '02': 'B', '03': 'C', '04': 'D', '05': 'E', '06': 'F', '07': 'G', '08': 'H',
            '09': 'I', '10': 'J', '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q',
            '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z',
            '27': '.', '28': ',', '29': '!', '30': '?'}

input_folder = 'E:\\ECOO\\Primetime\\Input\\DATA11.txt'
output_folder = 'E:\\ECOO\\Primetime\\Output\\DATA12.txt'

x = 1
with open('%s' % input_folder, 'r') as txt, open('%s' % output_folder, 'w') as txt2:
    txt.readline()
    for line in txt:
        line = line.replace('\n', '')
        text = line
        coded = text.rsplit(' ')
        try:
            key = 0
            while True:
                key = key + 1
                key_find = str(int(coded[1]) / key)
                # print('Current: %s' % modify)
                if '.0' in key_find:
                    if len(key_find) <= 6:
                        isPrime = True
                        for num in range(2, int(math.sqrt(key)) + 1):
                            if key % num == 0:
                                isPrime = False
                                break

                        if isPrime is True:
                            break

        except ValueError:
            pass
        for i in range(0, len(coded)):
            i = int(i)
            if i == 0:
                continue
            modify = int(coded[i]) / key
            modify = str(modify)
            modify = modify.replace('.0', '')
            if len(modify) < 4:
                modify = modify.replace('%s' % modify, '0%s' % modify)
            coded.pop(i)
            coded.insert(i, modify)
        coded.pop(0)
        library['Message%s' % x] = coded

        # modify = modify.replace('.0', '')

        x = x + 1
    for message in library:
        stringy = ''
        for bundle in library[message]:
            stringy = stringy + bundle
        c = 0
        decoded = ''
        print(stringy)
        while True:
            try:
                line = stringy[c] + stringy[c + 1]
                decoded = decoded + alphabet[line]
                c = c + 2
            except IndexError:
                break
        print(decoded)
        txt2.write('%s\n' % decoded)
txt.close(), txt2.close()