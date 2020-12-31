if float(current_t[0][0]) >= 0 and float(current_t[0][1]) >= 0:
    current_t.append(math.degrees(math.atan(float(current_t[0][1]) / float(current_t[0][0]))))
elif float(current_t[0][0]) < 0 and float(current_t[0][1]) > 0:
    current_t.append(math.degrees(math.atan(float(current_t[0][1]) / float(current_t[0][0]))))
elif float(current_t[0][0]) < 0 and float(current_t[0][1]) < 0:
    current_t.append(math.degrees(math.atan(float(current_t[0][1]) / float(current_t[0][0]))))
elif float(current_t[0][0]) >= 0 and float(current_t[0][1]) < 0:
    current_t.append(math.degrees(math.atan(float(current_t[0][1]) / float(current_t[0][0]))))