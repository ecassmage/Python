def fibonacci(x, lis={}):
    if x in lis:
        return lis[x]
    if x <= 1:
        return 1
    xy = fibonacci(x-1) + fibonacci(x-2)
    lis.update({x: xy})
    return xy


print(fibonacci(10))
print(fibonacci(10))
