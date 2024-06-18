def Test1():
    lst  = [1, 2, 3, 4, 5]

    for val in lst:
        print (val, end=' ')
    print()

    #######################

    length = len(lst)
    while length != 0:
        print(lst[length -1], end=' ')
        length -= 1
    print()

    ######################

    counter = 0
    while True:
        print(lst[counter], end=' ')
        counter += 1
        if counter >= len(lst):
            break
    print()

    ###########################
    '''
    counter = 0
    print("Data --> ", lst[7])
    while True:
        print(lst[counter], end=' ')
        counter += 1
    print()
    '''
    '''
    str1 = "String"
    print(str1[9])
    '''

def Test2():
    # iter() - Accepts and iterable and returns an iterator
    lst  = [1, 2, 3, 4, 5]
    # lst is an iterable
    # Using the iter(), we can get an iterator from an iterable
    # Below, it is the iterator that we get from lst, upon calling iter on lst

    it = iter(lst) # lst.__iter__()
    # Hence, to be an iterable, the type has to implement __iter__()


    # we can call next() upon the iterator, to get the next element
    # next(it) --> it.__next__()
    # meaning that every iterator needs to have implemented the __next__()
    # If iter() is called upon an iterator, then it returns self
    # iter(it) will return itself, as it is an iterator 

    # All iterators are iterable, but the reverse ma not be true always

    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it)) # Last element
    print(next(it))

def Test3():
    lst  = [1, 2, 3, 4, 5]

    it = iter(lst)
    try:
        while True:
            print(next(it))
    except StopIteration:
        print("Reached end of collection")


def IsIterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def Test4():
    print(IsIterable(list()))
    print(IsIterable(int()))


Test4()