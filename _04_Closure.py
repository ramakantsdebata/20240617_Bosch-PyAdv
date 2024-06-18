
# LEGB - Local, External, Global, Builtins

def Outer():
    x = 10
    def Inner():
        print("Inner", x)

    return Inner
    # Inner()

# fn1 = Outer()
# print("-" * 10)
# fn1()


def multiplier(num = 3):
    def Mult(x):
        return num * x

    return Mult

M2 = multiplier(2)
M3 = multiplier(3)
M4 = multiplier(4)

print(M2, M3, M4, sep="\n")
print(M2(10))
print(M3(10))
print(M4(10))
