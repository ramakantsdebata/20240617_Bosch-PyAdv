'''
def AddMethodDecorator(fn):
    def wrapper(*vArgs, **kwArgs):
        print(f"Calling {fn.__name__}")
        retVal = fn(*vArgs, **kwArgs)
        print(f"Returning from {fn.__name__}")
        return retVal
    return wrapper
'''



class AddMethodDecorator:
    def __init__(self, Method) -> None:
        self.Method = Method
        self.count = 0

    def __call__(self, *vArgs, **kwArgs):
        self.count += 1
        print(f"[{self.count}]Calling {self.Method.__name__}")
        retVal = self.Method(*vArgs, **kwArgs)
        return retVal


def sub(a, b):
    return a - b

dec = AddMethodDecorator(sub)
sub = dec


@AddMethodDecorator
def add(a, b):
    return a + b

@AddMethodDecorator
def mul(a, b):
    return a * b

#########################################

print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(1, 2))
print(add(1, 2))

print(mul(1, 2))
print(mul(1, 2))
print(mul(1, 2))
print(mul(1, 2))
print(mul(1, 2))

print(sub(2, 1))
print(sub(2, 1))


'''
class Interger:
    def __init__(self) -> None:
        pass

    def __call__(self, *args, **kwds):
        print("Called as a function")

obj = Interger()
obj() # obj.__call__(...)

# operator()(...)
# operator+(...)
'''
