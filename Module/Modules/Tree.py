flip = True


class Tree:
    def __init__(self, gen):
        self.parent = None
        self.gen = gen
        self.children = []

    def print_tree(self, extra=''):
        global flip
        if self.gen is not None:
            print(f'{extra}{self.gen}')
        if self.children:
            extra += '   '
            for child in self.children:
                flip = True
                child.print_tree(extra)
        if self.children and flip:
            flip = False
            print('')


def fam(x, parent=None):
    z = []
    for i in x:
        generation = i
        gen = Tree(generation)
        if isinstance(x[i], dict):
            y = fam(x[i], i)
            gen.children = y
        # temp = Tree(i)
        gen.parent = parent
        z.append(gen)
    return z


if __name__ == '__main__':
    family = {'Bob': {'Joe': {'John': None, 'Evan': None, 'Connor': None}, 'Jill': {'Jack': None, 'Brad': None}},
              'Carry': {'Fred': {'Rim': {'Marry': None, 'Sue': {'Harry': None}}}, 'Fiona': {'Bill': None, 'Garry': {'Harold': None}}, 'Manfred': {'Simon': {'Lewis': {'Chris': None}}}, 'Diego': None}}
    famoosh = fam(family)

    print(famoosh)
    for i in famoosh:
        i.print_tree()
else:
    print("This is not your world anymore")
