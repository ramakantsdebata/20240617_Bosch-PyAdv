def Log(fn):
    def Wrapper(*vArgs, **kwArgs):      # Packing the unknown arguments to vArgs and kwArgs
        print("Calling greet()")
        fn(*vArgs, **kwArgs)            # Unpacking vArgs and kwArgs
        print("Returning from greet()")
    return Wrapper

@Log
def greet():
    print("Hello")

@Log
def greetName(name):
    print(f"Hi {name}")

###########################################################

def Test1():
    greet()
    greetName("Ramakant")

Test1()