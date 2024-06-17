'''
# Define earlier vs Define Higher


def greet():
    print("Hello")

def Main():
    print("Main")
    Foo()

def Foo():
    print("Foo")
    Bar()
    print("Returning from Foo")

def Bar():
    print("Bar")

# print(f"__name__ --> {__name__}")

if __name__ == '__main__':
    Main()
'''

#################################################
'''
## Positional argument

def add( a, b, c = 0):
    print(f"a [{a}] + b [{b}] + c [{c}]= [{a + b + c}]")
    return a + b + c


# print(add(1, 2))
add(1, 2)
add(b = 2, a = 1)
add(1, 2, 3)
'''
##########################################################
'''
## Packing and UnPacking

lst = [1, 2, 3, 4, 5]

a, b, c, d, e = lst     # Unpacking
# a, b, c, d, e, f = lst
# a, b, c, d = lst

a, b, *others = lst

print(a, b, others, sep="\n")
print(type(others))


def add(a, b, c):
    return a + b + c

lst = [1, 2, 3]

print(add(lst[0], lst[1], lst[2]))
print(add(*lst))                        # Unpacking in the call


def mul(*data):
    l1 = list(data)
    print(type(data), data)
    prod = 1
    for x in data:
        prod *= x
    return prod

print("prod =", mul(*lst))
print("prod =", mul(1, 2, 3, 4))

print("prod =", mul(lst))  # <-- lst will just become one of the elements of data
'''

## Var Args #######################################################

def add(a, b, *data, **kwData):   # Var arg
    print(f"a[{a}], b[{b}], data[{data}], kwData[{kwData}]", end='--->')
    sum = a + b
    for x in data:
        sum += x
    return sum

def Test1():
    # print(add())
    # print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    print(add(1, 2, 3, 4))
    print(add(1, 2, 3, 4, 5, p = 6, q = 7, r = 8))

def Test2():
    lst = [1]
    print(type(lst), lst)

    tup = (1,)
    print(type(tup), tup)

def add(a, b, *data):   # Var arg
    print(f"a[{a}], b[{b}], data[{data}]", end='--->')
    sum = a + b
    for x in data:
        sum += x
    print(sum)
    return sum

def SomeFunction(*vargs, **kwargs):
    '''    
    for x in vargs:
        print(x, end='-')

    for x in kwargs.values():
        print(x, end='-')
    print()
    '''
    add(*vargs, **kwargs)


def Test3():
    SomeFunction(1, 2)
    SomeFunction(1, 2, 3)
    SomeFunction(1, 2, 3, 4)
    SomeFunction(1, 2, 3, 4, 5, p = 6, q = 7, r = 8)

from multipledispatch import dispatch

@dispatch(str)
def Print(name:str):
    print(name)

@dispatch(int, int)
def Print(a:int, b:int):
    print(a, b)

def Test4():
    # print(type(Print))
    Print(1, 2)
    Print("String")
    Print("Test", "String")

Test4()

'''
int Add(int a, int b) --> Add_int_int
{}

float Add(float a, float b) --> Add_float_float
{}

x = Add(1,2)    --> Add_int_int(1, 2)

Add(1.0, 2)
'''