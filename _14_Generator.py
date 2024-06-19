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


def FibGen(num):
    '''
    Fibonacci Series
    '''
    a, b  = 0, 1
    for i in range(num):
        yield a
        a, b = b, a+b

def Test2():
    it  = FibGen(10)

    try:
        while True:
            print(next(it), end = ' ')
    except StopIteration:
        print()

def Test3():
    for i in FibGen(10):
        print(i, end=' ')
    print()

Test3()