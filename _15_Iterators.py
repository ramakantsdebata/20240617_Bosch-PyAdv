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


Test1()