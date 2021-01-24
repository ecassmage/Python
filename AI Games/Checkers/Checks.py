from custom import isfloat, isbool, bubble_sort, issorted, fizzbuzz
import random
a = '1.9'
b = '5'
c = 'a'
d = '6.0'
e = .1
f = 0.0
g = 'True'
h = 'False'
i = '1'
j = '0'
sort_list = [34, 30, 75, 27, 8, 58, 10, 1, 59, 25]
loopy = [True, False, 'True', 'False', '1', '0', 1, 0, 2, -0.1, 'seven']
print(isfloat(a), isfloat(b), isfloat(c), isfloat(d), isfloat(e), isfloat(f))
print(isbool(g), isbool(h), isbool(i), isbool(j))
new_list = []
[new_list.append(random.randint(0, 1000)) for i in range(1000)]
print(bubble_sort(sort_list))
print(bubble_sort(new_list))
print(issorted(new_list))
new_list.append(500)
print(issorted(new_list))
fizzbuzz(100)