class FibGen:
    def __init__(self, num) -> None:
        self.num = num

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.count = 0
        return self

    def __next__(self):
        # for i in range(self.num)
        if self.count < self.num:
            x = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return x
        else:
            raise StopIteration


def Test1():
    fg = FibGen(10)

    for x in fg:
        print(x, end=' ')
    print()


    for x in fg:
        print(x, end=' ')
    print()

def Test2():

    for i in range(1, 30, 2):
        print(i, end=' ')
    print()

def Test4():
    it1  = iter(FibGen(10))
    it2  = iter(FibGen(10))

    try:
        while True:
            print(next(it1), end = '-')
            print(next(it2))
    except StopIteration:
        print()


Test4()