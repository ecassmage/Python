class ThisIsClass:
    def __init__(self, num, string, boolean):
        self.num = num
        self.string = string
        self.boolean = boolean
        

lis = [ThisIsClass(10, "hello", True), ThisIsClass(15, 'GoodBye', False)]
print(lis)
print(type(lis))
print(repr(lis))
