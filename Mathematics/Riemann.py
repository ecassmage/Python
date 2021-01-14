equation = {}
x = 0
intervals = 1
range_integral = [0, 10]


def print_formula(number, dictionary):
    for j, i in enumerate(reversed(dictionary)):
        if dictionary[i] == '0':
            number -= 1
            continue
        elif j == 0:
            sign = ''
        else:
            sign = ' + '
        if len(dictionary) - j - 1 > 1:
            ex = f'x^{number}'
        elif len(dictionary) - j - 1 == 1:
            ex = 'x'
        else:
            ex = ''
        next_sec = f'{sign}{dictionary[i]}{ex}'
        print(f'{next_sec}', end='')
        number -= 1
    print('')


def calcs(number, dictionary, int_range, inter):
    integrated_area = 0
    for corridor in range(range_integral[0], range_integral[1], intervals):
        current_value = 0
        for num_value, value in enumerate(dictionary):
            current_value += int(dictionary[value]) * (corridor ** num_value)
        integrated_area += intervals * current_value

        print(current_value)
    print(integrated_area)
    return integrated_area


while True:
    num = input("Please enter a number: ")
    try:
        if num == 'exit':
            break
        elif str(abs(int(num))).isdigit():
            if int(num) < 0:
                equation.update({'x%d' % x: f'({num})'})
            else:
                equation.update({'x%d' % x: num})
        else:
            continue
    except ValueError:
        continue
    x += 1
print(equation)
x -= 1
print_formula(x, equation)
back = calcs(x, equation, range_integral, intervals)
range_integral = [1, 11]
back2 = calcs(x, equation, range_integral, intervals)
print(back, back2, ((back + back2) / 2))