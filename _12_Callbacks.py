class Publisher:
    def __init__(self) -> None:
        self.func = []

    def AddFunction(self, fn):
        self.func.append(fn)

    def __str__(self):
        return f"Functions in the collection --> {self.func}"
    
    def __len__(self):
        return len(self.func)
    
    def RemoveFunction(self, fn):
        self.func.remove(fn)

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

pub1[0]