class Publisher:
    def __init__(self) -> None:
        self.collFn = []

    def AddFunction(self, fn):
        self.collFn.append(fn)

    def __str__(self):
        return f"Functions in the collection --> {self.collFn}"
    
    def __len__(self):
        return len(self.collFn)
    
    def __getitem__(self, idx):
        return self.collFn[idx]
    
    def RemoveFunction(self, fn):
        self.collFn.remove(fn)

    def NotifyAll(self, data):
        for i in range(len(self)):
            self[i](data)


#############################################

def Foo(data):
    print("Foo -", data)

def Bar(data):
    print("Bar -", data)

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

try:
    pub1[0]("StringData")
except IndexError as ex:
    print(f"{ex!r}")

print("Resuming normal functioning")
pub1.AddFunction(Foo)
pub1.NotifyAll("Time to wrap up")