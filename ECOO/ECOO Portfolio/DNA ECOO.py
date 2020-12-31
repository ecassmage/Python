import re
import os

input_folder = 'E:\\ECOO\\DNA\\Input\\DATA21.txt'
output_folder = 'E:\\ECOO\\DNA\\Output\\DATA22.txt'
DNA_list = []
position = 0


def splicer(event, tick):
    splice = event.replace('A', 'w')
    splice = splice.replace('T', 'x')
    splice = splice.replace('C', 'y')
    splice = splice.replace('G', 'z')

    if tick == 1:
        splice = splice.replace('w', 'u')

    splice = splice.replace('u', 'U')
    splice = splice.replace('w', 'T')
    splice = splice.replace('x', 'A')
    splice = splice.replace('y', 'G')
    splice = splice.replace('z', 'C')

    return splice


if os.path.exists(output_folder):
    os.remove(output_folder)

with open(input_folder, 'r') as input_file:
    letter_list = []
    txt = input_file.readlines()

    for line in txt:

        DNA_list.append(line)
        line = line.split('TATAAT')
        line = line[1]
        cut = line[:4]
        line = re.sub('%s' % cut, '', line)
        liner = line
        liner = liner.replace('\n', '')
        fact = splicer(liner, 0)
        c = 0
        seven = 6

        while True:
            sequence = fact[c + 5] + fact[c + 4] + fact[c + 3] + fact[c + 2] + fact[c + 1] + fact[c]

            c = c + 1
            result = liner.find(sequence)

            if sequence in liner:

                if c < 5:
                    pass

                else:

                    while True:

                        if (fact[c + 5] + sequence) in liner:
                            sequence = fact[c + 5] + sequence
                            c = c + 1

                        else:
                            sequence = sequence[::-1]
                            break
                    break
            else:
                pass
        sequence = splicer(sequence, 0)
        position = position + 1
        transcription = splicer(liner.split(sequence)[0], 1)
        print('%s: %s' % (position, transcription))
        transcription2 = liner.split(sequence)[0]

        with open(output_folder, 'a') as output_file:
            output_file.write('%s: %s\n' % (position, transcription))
    output_file.close()
    input_file.close()


