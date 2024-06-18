def repeat(n):
    def wrapper1(fn):
        def wrapper2(*vArgs, **kwArgs):
            for _ in range(n):
                fn(*vArgs, **kwArgs)
        return wrapper2
    return wrapper1

def log_with_level(level= "info"):
    def wrapper1(fn):
        def wrapper2(*vArgs, **kwArgs):
            print(f"[{level.upper()}]: Calling '{fn.__name__}' with args: {vArgs} and {kwArgs}")
            fn(*vArgs, **kwArgs)
            print(f"[{level.upper()}]: Returning from'{fn.__name__}' with args: {vArgs} and {kwArgs}")
        return wrapper2
    return wrapper1


# @repeat(5)
@log_with_level("debug")
def printStr(string):
    try:
        print(string)
        raise Exception("Just like that")
        return
    except Exception as ex:
        print(f"{ex!r}")


######################################

def Test1():
    try:
        printStr("NewLine")
    except Exception as ex:
        print(f"{ex!r}")

Test1()

'''
def SomeFunc(*vArgs, **kwArgs):
    for x in vArgs:
        print(x, end=' ')
    print()
    for x in kwArgs.items():
        print(x, end=' ')
    print("\n\n")


SomeFunc()
SomeFunc(1)
SomeFunc(1, 2, 3)
SomeFunc(a = 1, b =2, c = 3)
SomeFunc(1, 2, 3, p = 4, q = 5, r = 6)
'''
