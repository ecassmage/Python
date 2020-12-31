import math
input_folder = 'E:\\ECOO\\Triangles\\Input\\DATA31.txt'
output_folder = 'E:\\ECOO\\Triangles\\Output\\DATA32.txt'

with open('%s' % input_folder, 'r') as txt, open('%s' % output_folder, 'w') as txt2:
    txt.readline()
    for i in txt:
        current_t = []
        i = str(i).replace('\n', '')
        current_t.append(i.split(' '))
        # print(i)
        current_t.append(math.sqrt(math.pow(float(current_t[0][0]), 2) + math.pow(float(current_t[0][1]), 2)))
        # print(current_t[0])
        if float(current_t[0][0]) >= 0 and float(current_t[0][1]) >= 0:
            current_t.append(math.degrees(math.atan(float(current_t[0][1]) / float(current_t[0][0]))))
        elif float(current_t[0][0]) < 0 and float(current_t[0][1]) > 0:
            current_t.append(math.degrees(math.atan(float(current_t[0][1]) / float(current_t[0][0]))) + 180)
        elif float(current_t[0][0]) < 0 and float(current_t[0][1]) < 0:
            current_t.append(math.degrees(math.atan(float(current_t[0][1]) / float(current_t[0][0]))) + 180)
        elif float(current_t[0][0]) > 0 and float(current_t[0][1]) < 0:
            current_t.append(math.degrees(math.atan(float(current_t[0][1]) / float(current_t[0][0]))) + 360)
        s_d = float(current_t[2]) - 60
        current_t.append(s_d)
        point_1 = float(current_t[1]) * math.cos(math.radians(current_t[3]))
        point_2 = float(current_t[1]) * math.sin(math.radians(current_t[3]))
        # print(point_1, point_2)
        s_d = float(s_d) + 120
        point_3 = point_1 + (2 * float(current_t[1])) * math.cos(math.radians(s_d))
        point_4 = point_2 + (2 * float(current_t[1])) * math.sin(math.radians(s_d))
        # print(point_3, point_4)
        s_d = s_d + 120
        point_5 = point_3 + (2 * float(current_t[1])) * math.cos(math.radians(s_d))
        point_6 = point_4 + (2 * float(current_t[1])) * math.sin(math.radians(s_d))
        # print(point_5, point_6)
        point_1 = format(point_1, '.1f')
        point_2 = format(point_2, '.1f')
        point_3 = format(point_3, '.1f')
        point_4 = format(point_4, '.1f')
        point_5 = format(point_5, '.1f')
        point_6 = format(point_6, '.1f')
        txt2.write('(%s,%s) (%s,%s) (%s,%s)\n' % (point_5, point_6, point_1, point_2, point_3, point_4))
        # print(current_t)
        print('(%s,%s) (%s,%s) (%s,%s)' % (point_5, point_6, point_1, point_2, point_3, point_4))
