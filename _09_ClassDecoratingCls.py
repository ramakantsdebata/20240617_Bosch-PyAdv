
class AddClsDecorator:
    def __init__(self, cls) -> None:
        self.cls = cls
        self.AddAttribs("Pune")

    def AddAttribs(self, value):
        self.cls.city = value

    def __call__(self, *args, **kwds):
        return self.cls(*args, **kwds)

@AddClsDecorator
class MyClass:
    def __init__(self, name) -> None:
        self.name = name

    def Display(self):
        print(f"{self.__dict__.values()}")

def Consumer():
    obj1 = MyClass("Manish")
    print(obj1.name)
    print(obj1.city)

Consumer()

