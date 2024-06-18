class Publisher:
    def __init__(self) -> None:
        self.collFn = []

    def AddFunction(self, fn):
        self.collFn.append(fn)

    def __str__(self):
        return f"Functions in the collection --> {self.collFn}"
    
    def __len__(self):
        return len(self.collFn)
    
    def RemoveFunction(self, fn):
        self.collFn.remove(fn)

#############################################

def Foo():
    print("Foo")

def Bar():
    print("Bar")

pub1 = Publisher()
pub1.AddFunction(Foo)
pub1.AddFunction(Bar)
print(len(pub1)) # pub1.__len__()
print(pub1)
# print(str(pub1))
# print(pub1.__str__())
# print(pub1.__repr__())

pub1.RemoveFunction(Foo)
print(pub1)

pub1[0]()