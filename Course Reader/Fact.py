def fact(n):
    x = 1
    for i in range(n+1):
        x *= i
        if x == 0:
            x = 1
    return x


string = "Words Heret"
print(fact(300) / (fact(6) * fact(300-6)))
listExample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if 't' in string:
    pass
indexPos = listExample.index(4)
print(indexPos)
# indexPos = listExample.index(11)
print(indexPos)
print(string.index('t'))
print(string.find('tt'))
