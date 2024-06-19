class TestType:
    p = 10
    q = 20

    def __init__(self) -> None:
        self.a = 0
        self.b = 1
        self.result = 100


    def instanceMethod(self):
        print("InstanceMethod", self.a, self.b)

    @classmethod
    def classMethod(cls):
        print("ClassMethod", cls.p, cls.q)

    @staticmethod
    def staticMethod():
        print("StaticMethiod", )

    def __del__(self):
        print("__del__ called")

    def __delete__(self, instance):
        print("__delete__ called")
        print(f"instance [{hex(id(instance))}], Self [{hex(id(self))}]")
        instance.res = self.result


class Container:
    m_test = TestType()

    def __init__(self) -> None:
        self._test = TestType()
        self.res = 0

def Test1():
    # TestType.classMethod()
    obj = TestType()
    print(obj.__class__.__name__)
    obj.instanceMethod()
    obj.classMethod()
    TestType.classMethod()

    TestType.staticMethod()
    obj.staticMethod()


t1: TestType

def Test2():
    global t1
    obj = TestType()
    t1 = obj



def Test3():
    c1 = Container()
    print(f"c1 [{hex(id(c1))}], c1.m_test [{hex(id(c1.m_test))}]")
    # del c1
    # del c1._test
    # del Container.m_test
    del c1.m_test
    print(c1.res)




Test3()
print("Program end")



'''
from  random import randint

class Container:
    def __init__(self, size, bAC, bHeating, bInter) -> None:
        self.serial = Container.generateSerial(size, bAC, bHeating, bInter)

    @staticmethod
    def generateSerial(size, bAC, bHeating, bInter):
        # Generate the serial

        return randint(1, 100)


def Consumer():
    c1 = Container(size = s1, bAC = True, bHeating = False, bInter = True)

'''