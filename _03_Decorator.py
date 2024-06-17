def Log(fn):
    def Wrapper():
        print("Calling greet()")
        fn()
        print("Returning from greet()")
    return Wrapper

def greet():
    print("Hello")

greet = Log(greet)


###########################################################

def Test1():
    greet()
    # Wrap()

Test1()