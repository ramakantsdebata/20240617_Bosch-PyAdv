def SimpleGen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

def Test1():
    it = SimpleGen()
    print(type(it))

    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

Test1()